from __future__ import annotations

import asyncio
import base64
import json
import threading
import time
from contextlib import contextmanager
from pathlib import Path

import httpx
import pytest
from websockets.sync.server import serve

from qca import AsyncForward, AuthenticationError, ConflictError, Forward, Managed
from qca.forward import (
    RealtimeError,
    RealtimeProtocolError,
    RealtimeQueueOverflowError,
    RealtimeServerError,
    RealtimeTimeoutError,
)
from qca.forward.resources.realtime._protocol import encode_event, parse_event
from qca.forward.types.realtime import RealtimeAudioPayload, RealtimeReadyPayload

FIXTURE = json.loads((Path(__file__).parent / "fixtures/realtime.json").read_text())
EVENTS = {event["type"]: event for event in FIXTURE["events"]}


def event(type_, payload=None, **kwargs):
    return {**EVENTS[type_], **kwargs, **({"payload": payload} if payload is not None else {})}


@contextmanager
def server(handler, *, process_request=None):
    with serve(handler, "127.0.0.1", 0, process_request=process_request, close_timeout=0.2) as ws:
        thread = threading.Thread(target=ws.serve_forever, daemon=True)
        thread.start()
        try:
            yield f"http://127.0.0.1:{ws.socket.getsockname()[1]}/prefix/api/v1/forward/", ws
        finally:
            ws.shutdown()
            thread.join(timeout=2)


def ready(socket):
    socket.send(json.dumps(event("voice.state")))
    socket.send(json.dumps(event("voice.ready")))


@pytest.mark.parametrize("row", FIXTURE["events"], ids=lambda r: r["type"])
def test_event_protocol_types_and_extensions(row):
    parsed = parse_event(json.dumps(row), "conv_fixture")
    assert parsed.timestamp == "2026-10-13T01:02:03.123456789Z"
    assert parsed.to_dict()["future_envelope"] == "preserved"
    for key, value in row["payload"].items():
        assert parsed.to_dict()["payload"][key] == value
    if parsed.type == "audio.delta":
        assert isinstance(parsed.payload, RealtimeAudioPayload)
        assert parsed.audio_bytes() == b"\x01\x00\x02\x00"
    if parsed.type == "voice.ready":
        assert isinstance(parsed.payload, RealtimeReadyPayload)


@pytest.mark.parametrize(
    "message",
    [
        b"{}",
        "{}",
        "[]",
        "invalid",
        json.dumps({**EVENTS["pong"], "version": "wrong"}),
        json.dumps({**EVENTS["pong"], "sequence": True}),
        json.dumps({**EVENTS["pong"], "conversation_id": "other"}),
        json.dumps({**EVENTS["voice.ready"], "payload": {}}),
        json.dumps({**EVENTS["pong"], "timestamp": "bad"}),
    ],
)
def test_bad_server_envelopes_fail(message):
    with pytest.raises(RealtimeProtocolError):
        parse_event(message, "conv_fixture")


@pytest.mark.parametrize("async_", [False, True])
async def test_create_history_auth_and_independent_pagination(async_):
    calls = []

    def handle(request):
        calls.append(request)
        if request.method == "POST":
            return httpx.Response(201, json=FIXTURE["conversation"], headers={"x-request-id": "req_create"})
        data = json.loads(json.dumps(FIXTURE["history"]))
        if request.url.params.get("before"):
            data["events"] = []
            data["page"] = {"next_before": None, "has_more": False}
        return httpx.Response(200, json=data, headers={"x-request-id": "req_history"})

    http_client = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = (AsyncForward if async_ else Forward)(
        access_token="sat_fixture",
        auth_mode="sa",
        base_url="https://api.test/prefix/api/v1/forward/",
        http_client=http_client,
        _strict_response_validation=True,
    )
    try:
        result = client.realtime.conversations.create(
            identity_id="idn_1",
            template_id="tmpl_1",
            idempotency_key="stable-key",
            config={"audio": {"output": {"voice": "longanlingxin"}}},
        )
        result = await result if async_ else result
        assert result.id == "conv_fixture" and result._request_id == "req_create"
        assert calls[0].url.path == "/prefix/api/v1/forward/realtime/conversations"
        assert calls[0].headers["idempotency-key"] == "stable-key"
        assert calls[0].headers["authorization"] == "Bearer sat_fixture"
        assert json.loads(calls[0].content) == {
            "identity_id": "idn_1",
            "template_id": "tmpl_1",
            "config": {"audio": {"output": {"voice": "longanlingxin"}}},
        }
        page = client.realtime.conversations.history("conv/encoded", limit=2, types="work")
        page = await page if async_ else page
        assert page.events[0].id == "vevt_1" and page.events[0].to_dict()["future_history_field"] == "preserved"
        assert page.has_next_page()
        older = page.get_next_page()
        older = await older if async_ else older
        assert not older.has_next_page()
        with pytest.raises(RuntimeError):
            result = older.get_next_page()
            if async_:
                await result
        assert calls[-1].url.params == httpx.QueryParams({"limit": 2, "before": "cursor_old", "types": "work"})
        assert b"conv%2Fencoded" in calls[-1].url.raw_path
    finally:
        if async_:
            await client.close()
        else:
            client.close()


@pytest.mark.parametrize("key", ["", " space", "space ", "x" * 257, "中" * 86, "bad\nvalue"])
def test_invalid_idempotency_before_network(key):
    with Forward(
        pat="test", http_client=httpx.Client(transport=httpx.MockTransport(lambda r: pytest.fail("network")))
    ) as client:
        with pytest.raises(ValueError):
            client.realtime.conversations.create(identity_id="idn_1", template_id="tmpl_1", idempotency_key=key)


@pytest.mark.parametrize("query", [{"limit": 0}, {"limit": 101}, {"limit": True}, {"before": ""}, {"types": "other"}])
def test_history_query_validation(query):
    with Forward(
        pat="test", http_client=httpx.Client(transport=httpx.MockTransport(lambda r: pytest.fail("network")))
    ) as client:
        with pytest.raises(ValueError):
            client.realtime.conversations.history("conv", **query)


def test_creation_retries_reuse_key_but_conflict_is_not_retried(monkeypatch):
    calls = []

    def handle(request):
        calls.append(request)
        if len(calls) == 1:
            return httpx.Response(
                503,
                json={"error": {"code": "idempotency_unavailable", "message": "retry"}},
                headers={"Retry-After": "0.001"},
            )
        return httpx.Response(201, json=FIXTURE["conversation"])

    with Forward(pat="test", http_client=httpx.Client(transport=httpx.MockTransport(handle))) as client:
        client.realtime.conversations.create(identity_id="idn", template_id="tmpl", idempotency_key="stable")
        assert len(calls) == 2 and calls[0].content == calls[1].content
        assert {r.headers["idempotency-key"] for r in calls} == {"stable"}
    calls.clear()

    def conflict(request):
        calls.append(request)
        return httpx.Response(
            409,
            json={"error": {"code": "idempotency_key_in_progress", "message": "pending"}},
            headers={"Retry-After": "2", "X-Request-Id": "req_conflict"},
        )

    with Forward(pat="test", http_client=httpx.Client(transport=httpx.MockTransport(conflict))) as client:
        with pytest.raises(ConflictError) as caught:
            client.realtime.conversations.create(identity_id="idn", template_id="tmpl", idempotency_key="stable")
        assert caught.value.code == "idempotency_key_in_progress" and caught.value.request_id == "req_conflict"
        assert caught.value.response.headers["retry-after"] == "2" and len(calls) == 1


@pytest.mark.parametrize("async_", [False, True])
async def test_local_websocket_ready_events_send_and_graceful_close(async_):
    recorded = []

    def handler(socket):
        recorded.append(socket.request)
        ready(socket)
        for raw in socket:
            incoming = json.loads(raw)
            recorded.append(incoming)
            assert incoming["version"] == "voice.realtime.v1"
            if incoming["type"] == "ping":
                socket.send(json.dumps(event("pong")))
            if incoming["type"] == "text.message":
                socket.send(json.dumps(event("transcript.final", {"role": "assistant", "text": "response"})))
            if incoming["type"] == "connection.close":
                socket.send(
                    json.dumps(
                        event(
                            "connection.closed", {"request_id": incoming["payload"]["request_id"], "outcome": "saved"}
                        )
                    )
                )

    with server(handler) as (base_url, _):
        client = (AsyncForward if async_ else Forward)(pat="pat_fixture", base_url=base_url, timeout=0.001)
        connection = client.realtime.connect(conversation_id="conv_fixture", proxy=None)
        connection = await connection if async_ else connection
        try:
            assert connection.ready.provider == "qoder"
            for expected in ("voice.state", "voice.ready"):
                value = connection.recv(timeout=1)
                value = await value if async_ else value
                assert value.type == expected
            for name, args in [
                ("send_text", ("hello",)),
                ("append_audio", (b"\x01\x00\x02\x00",)),
                ("interrupt", ()),
                ("playback_started", ()),
                ("playback_ended", ()),
                ("playback_cancelled", ()),
                ("ping", ()),
            ]:
                result = getattr(connection, name)(*args)
                if async_:
                    await result
            result = connection.recv(timeout=1)
            result = await result if async_ else result
            assert result.type == "transcript.final"
            result = connection.recv(timeout=1)
            result = await result if async_ else result
            assert result.type == "pong"
            outcome = connection.close_gracefully(request_id="close_1")
            outcome = await outcome if async_ else outcome
            assert outcome == "saved"
            request = recorded[0]
            assert request.path == "/prefix/api/v1/forward/realtime?conversation_id=conv_fixture"
            assert request.headers["authorization"] == "Bearer pat_fixture"
            assert "pat_fixture" not in request.path
            assert all("access_token" not in r.get("payload", {}) for r in recorded[1:])
            assert any(
                r["type"] == "audio.append" and base64.b64decode(r["payload"]["audio"]) == b"\x01\x00\x02\x00"
                for r in recorded[1:]
            )
        finally:
            if async_:
                await connection.close()
                await client.close()
                assert connection._reader.done()
            else:
                connection.close()
                client.close()
                assert not connection._reader.is_alive()


@pytest.mark.parametrize("async_", [False, True])
async def test_dynamic_credentials_refresh_for_each_new_connection_and_header_priority(async_, monkeypatch):
    monkeypatch.setenv("QODER_PAT", "ambient_pat")
    calls = []

    class Credential:
        def get_token(self):
            calls.append(len(calls) + 1)
            return f"sat_{len(calls)}"

    observed = []

    def handler(socket):
        observed.append(socket.request.headers["authorization"])
        ready(socket)
        for _ in socket:
            pass

    with server(handler) as (base_url, _):
        client = (AsyncForward if async_ else Forward)(auth_mode="sa", credential=Credential(), base_url=base_url)
        try:
            for number in (1, 2):
                connection = client.realtime.connect(conversation_id="conv_fixture", proxy=None)
                connection = await connection if async_ else connection
                if async_:
                    await connection.close()
                else:
                    connection.close()
                assert observed[-1] == f"Bearer sat_{number}"
            connection = client.realtime.connect(
                conversation_id="conv_fixture", extra_headers={"authorization": "Bearer override"}, proxy=None
            )
            connection = await connection if async_ else connection
            if async_:
                await connection.close()
            else:
                connection.close()
            assert observed[-1] == "Bearer override" and len(calls) == 2
        finally:
            if async_:
                await client.close()
            else:
                client.close()


async def test_async_credential_and_cancellation_cleanup():
    called = []
    closed = threading.Event()

    class Credential:
        async def get_token(self):
            called.append(True)
            return "async_sat"

    def handler(socket):
        assert socket.request.headers["authorization"] == "Bearer async_sat"
        try:
            for _ in socket:
                pass
        finally:
            closed.set()

    with server(handler) as (base_url, _):
        async with AsyncForward(auth_mode="sa", credential=Credential(), base_url=base_url) as client:
            task = asyncio.create_task(client.realtime.connect(conversation_id="conv_fixture", proxy=None))
            while not called:
                await asyncio.sleep(0.001)
            await asyncio.sleep(0.05)
            task.cancel()
            with pytest.raises(asyncio.CancelledError):
                await task
            assert await asyncio.to_thread(closed.wait, 1)
            assert not [
                task for task in asyncio.all_tasks() if task.get_name() == "qca-realtime-reader" and not task.done()
            ]


@pytest.mark.parametrize("async_", [False, True])
async def test_handshake_status_errors_and_redirects_not_followed(async_):
    reached = []

    def forbidden(connection, request):
        reached.append(request)
        response = connection.respond(401, json.dumps({"code": "TOKEN_INVALID", "message": "expired"}))
        response.headers["x-request-id"] = "req_handshake"
        return response

    with server(lambda socket: pytest.fail("upgraded"), process_request=forbidden) as (base_url, _):
        client = (AsyncForward if async_ else Forward)(pat="secret_fixture", base_url=base_url)
        try:
            with pytest.raises(AuthenticationError) as caught:
                result = client.realtime.connect(conversation_id="conv_fixture", proxy=None)
                if async_:
                    await result
            assert caught.value.status_code == 401 and caught.value.code == "TOKEN_INVALID"
            assert caught.value.request_id == "req_handshake" and "secret_fixture" not in str(caught.value)
        finally:
            if async_:
                await client.close()
            else:
                client.close()
    assert len(reached) == 1
    redirected = []

    def redirect(connection, request):
        redirected.append(request)
        response = connection.respond(302, "redirect")
        response.headers["Location"] = "ws://127.0.0.1:1/destination"
        return response

    with server(lambda socket: pytest.fail("upgraded"), process_request=redirect) as (base_url, _):
        client = (AsyncForward if async_ else Forward)(pat="secret_fixture", base_url=base_url)
        try:
            with pytest.raises(Exception) as caught:
                result = client.realtime.connect(conversation_id="conv_fixture", proxy=None)
                if async_:
                    await result
            assert getattr(caught.value, "status_code", None) == 302
        finally:
            if async_:
                await client.close()
            else:
                client.close()
    assert len(redirected) == 1


@pytest.mark.parametrize("async_", [False, True])
async def test_ready_timeout_closes_transport(async_):
    closed = threading.Event()

    def handler(socket):
        socket.send(json.dumps(event("voice.state")))
        try:
            for _ in socket:
                pass
        finally:
            closed.set()

    with server(handler) as (base_url, _):
        client = (AsyncForward if async_ else Forward)(pat="test", base_url=base_url)
        try:
            with pytest.raises(RealtimeTimeoutError) as caught:
                result = client.realtime.connect(conversation_id="conv_fixture", ready_timeout=0.03, proxy=None)
                if async_:
                    await result
            assert caught.value.stage == "ready" and closed.wait(1)
        finally:
            if async_:
                await client.close()
            else:
                client.close()


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("mode", ["mismatch", "persistence_error", "invalid_outcome"])
async def test_graceful_close_requires_matching_success_ack(async_, mode):
    def handler(socket):
        ready(socket)
        for raw in socket:
            incoming = json.loads(raw)
            if incoming["type"] == "connection.close":
                if mode == "persistence_error":
                    socket.send(
                        json.dumps(
                            event(
                                "error", {"code": "event_persistence_failed", "message": "storage", "retryable": False}
                            )
                        )
                    )
                else:
                    socket.send(
                        json.dumps(
                            event(
                                "connection.closed",
                                {
                                    "request_id": "wrong" if mode == "mismatch" else incoming["payload"]["request_id"],
                                    "outcome": "failed" if mode == "invalid_outcome" else "saved",
                                },
                            )
                        )
                    )

    with server(handler) as (base_url, _):
        client = (AsyncForward if async_ else Forward)(pat="test", base_url=base_url)
        connection = client.realtime.connect(conversation_id="conv_fixture", proxy=None)
        connection = await connection if async_ else connection
        try:
            expected = {
                "mismatch": RealtimeTimeoutError,
                "persistence_error": RealtimeServerError,
                "invalid_outcome": RealtimeProtocolError,
            }[mode]
            with pytest.raises(expected):
                result = connection.close_gracefully(request_id="expected", timeout=0.04)
                if async_:
                    await result
            assert connection._closed
        finally:
            if async_:
                await connection.close()
                await client.close()
            else:
                connection.close()
                client.close()


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("mode", ["replace", "nonterminal", "overflow", "byte_budget", "malformed"])
async def test_receive_lifecycle_and_bounded_queue(async_, mode):
    def handler(socket):
        ready(socket)
        for raw in socket:
            if json.loads(raw)["type"] == "ping":
                if mode == "replace":
                    socket.send(json.dumps(event("voice.replaced")))
                elif mode == "nonterminal":
                    socket.send(json.dumps(event("error")))
                    socket.send(json.dumps(event("work.failed")))
                    socket.send(json.dumps(event("pong")))
                elif mode == "malformed":
                    socket.send("{")
                else:
                    for _ in range(8):
                        socket.send(json.dumps(event("pong")))

    with server(handler) as (base_url, _):
        client = (AsyncForward if async_ else Forward)(pat="test", base_url=base_url)
        connection = client.realtime.connect(
            conversation_id="conv_fixture",
            max_queue=2 if mode == "overflow" else 256,
            max_queue_bytes=1300 if mode == "byte_budget" else 4194304,
            proxy=None,
        )
        connection = await connection if async_ else connection
        try:
            for _ in range(2):
                result = connection.recv(timeout=1)
                if async_:
                    await result
            result = connection.ping()
            if async_:
                await result
            if async_:
                await asyncio.sleep(0.04)
            else:
                time.sleep(0.04)
            if mode == "nonterminal":
                for type_ in ("error", "work.failed", "pong"):
                    result = connection.recv(timeout=1)
                    result = await result if async_ else result
                    assert result.type == type_
                assert not connection._closed
            else:
                expected = (
                    RealtimeProtocolError
                    if mode == "malformed"
                    else RealtimeQueueOverflowError
                    if mode in ("overflow", "byte_budget")
                    else RealtimeError
                )
                with pytest.raises(expected):
                    for _ in range(10):
                        result = connection.recv(timeout=1)
                        if async_:
                            await result
                with pytest.raises(RealtimeError):
                    result = connection.send_text("after close")
                    if async_:
                        await result
        finally:
            if async_:
                await connection.close()
                await client.close()
            else:
                connection.close()
                client.close()


@pytest.mark.parametrize(
    "type_,payload",
    [
        ("text.message", {"text": ""}),
        ("text.message", {"text": "中" * 5462}),
        ("audio.append", {"audio": ""}),
        ("connection.close", {"request_id": " bad"}),
        ("connection.close", {"request_id": "中" * 43}),
        ("playback.started", {"work_id": ""}),
        ("custom", {"data": "x" * 262144}),
    ],
)
def test_outgoing_boundaries(type_, payload):
    with pytest.raises(ValueError):
        encode_event(type_, payload)


def test_protocol_pcm_and_playback_identity():
    payload = {"work_id": "work_1", "announcement_id": "ann_1", "future": True}
    assert json.loads(encode_event("playback.started", payload))["payload"] == payload
    with Managed(pat="test") as client:
        assert not hasattr(client, "realtime")


@pytest.mark.parametrize(
    "timestamp", ["2026-10-13", "2026-10-13T01:02:03", "2026-02-30T01:02:03Z", "2026-10-13T01:02:03+0000"]
)
def test_timestamp_requires_rfc3339_timezone(timestamp):
    with pytest.raises(RealtimeProtocolError):
        parse_event(json.dumps({**EVENTS["pong"], "timestamp": timestamp}), "conv_fixture")


@pytest.mark.parametrize("audio", ["", "AA=="])
def test_audio_requires_complete_pcm16(audio):
    with pytest.raises(RealtimeProtocolError):
        parse_event(json.dumps(event("audio.delta", {"audio": audio})), "conv_fixture")
    with pytest.raises(ValueError):
        encode_event("audio.append", {"audio": audio})


@pytest.mark.parametrize("async_", [False, True])
async def test_history_detects_cycles_and_raw_pages_are_bound(async_):
    calls = []

    def handle(request):
        calls.append(request)
        return httpx.Response(200, json=FIXTURE["history"])

    http_client = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = (AsyncForward if async_ else Forward)(pat="test", http_client=http_client)
    try:
        response = client.realtime.conversations.with_raw_response.history("conv_fixture")
        response = await response if async_ else response
        page = response.parse()
        page = await page if async_ else page
        older = page.get_next_page()
        older = await older if async_ else older
        with pytest.raises(RuntimeError, match="repeated"):
            result = older.get_next_page()
            if async_:
                await result
        assert len(calls) == 2
    finally:
        if async_:
            await response.close()
            await client.close()
        else:
            response.close()
            client.close()


@pytest.mark.parametrize("async_", [False, True])
async def test_server_can_disable_graceful_close(async_):
    def handler(socket):
        payload = json.loads(json.dumps(EVENTS["voice.ready"]["payload"]))
        payload["capabilities"]["graceful_close"] = False
        socket.send(json.dumps(event("voice.ready", payload)))
        for _ in socket:
            pass

    with server(handler) as (base_url, _):
        client = (AsyncForward if async_ else Forward)(pat="test", base_url=base_url)
        connection = client.realtime.connect(conversation_id="conv_fixture", proxy=None)
        connection = await connection if async_ else connection
        try:
            with pytest.raises(RealtimeError, match="does not support"):
                result = connection.close_gracefully()
                if async_:
                    await result
        finally:
            if async_:
                await connection.close()
                await client.close()
            else:
                connection.close()
                client.close()


@pytest.mark.parametrize("async_", [False, True])
async def test_handshake_budget_includes_credential_resolution(async_):
    from qca import APITimeoutError

    class Credential:
        def get_token(self):
            time.sleep(0.1)
            return "late_sat"

    reached = []
    with server(lambda socket: reached.append(True)) as (base_url, _):
        client = (AsyncForward if async_ else Forward)(credential=Credential(), auth_mode="sa", base_url=base_url)
        start = time.monotonic()
        try:
            with pytest.raises(APITimeoutError):
                result = client.realtime.connect(conversation_id="conv_fixture", handshake_timeout=0.01, proxy=None)
                if async_:
                    await result
            assert time.monotonic() - start < 0.09 and not reached
        finally:
            if async_:
                await client.close()
            else:
                client.close()


def test_text_trimming_and_riff_prefix_are_not_false_pcm_rejections():
    from qca.forward.resources.realtime._protocol import pcm_payload

    assert (
        json.loads(encode_event("text.message", {"text": " " * 20000 + "hello" + " " * 20000}))["payload"]["text"]
        == "hello"
    )
    assert base64.b64decode(pcm_payload(b"RIFF")["audio"]) == b"RIFF"
    with pytest.raises(ValueError):
        pcm_payload(b"RIFF" + b"\x00" * 4 + b"WAVE")


@pytest.mark.parametrize(
    "missing",
    [
        "QODER_FORWARD_GLOBAL_PAT",
        "QODER_SA_GLOBAL_KEY",
        "QODER_REALTIME_GLOBAL_SA_TEMPLATE_ID",
        "QODER_REALTIME_LIVE_ALLOW_WRITE",
        "QODER_REALTIME_LIVE_ALLOW_EXECUTION",
    ],
)
def test_live_configuration_preflights_all_selected_regions_before_requests(tmp_path, missing):
    from tests.realtime.config import realtime_environment

    environment = {
        "QODER_REALTIME_LIVE_ALLOW_WRITE": "true",
        "QODER_REALTIME_LIVE_ALLOW_EXECUTION": "true",
        "QODER_FORWARD_CN_PAT": "fixture_pat_cn",
        "QODER_FORWARD_GLOBAL_PAT": "fixture_pat_global",
        "QODER_SA_CN_KEY": "fixture_sa_cn",
        "QODER_SA_GLOBAL_KEY": "fixture_sa_global",
        "QODER_REALTIME_CN_PAT_TEMPLATE_ID": "tmpl_cn_pat",
        "QODER_REALTIME_CN_SA_TEMPLATE_ID": "tmpl_cn_sa",
        "QODER_REALTIME_GLOBAL_PAT_TEMPLATE_ID": "tmpl_global_pat",
        "QODER_REALTIME_GLOBAL_SA_TEMPLATE_ID": "tmpl_global_sa",
    }
    del environment[missing]
    with pytest.raises(ValueError, match=missing):
        realtime_environment(
            tmp_path / "unused.env", environment, [("cn", "pat"), ("cn", "sa"), ("global", "pat"), ("global", "sa")]
        )


@pytest.mark.parametrize("region", ["cn", "global"])
def test_live_configuration_accepts_explicit_forward_sat_without_platform_key(tmp_path, region):
    from tests.realtime.config import realtime_environment

    environment = {
        "QODER_REALTIME_LIVE_ALLOW_WRITE": "true",
        "QODER_REALTIME_LIVE_ALLOW_EXECUTION": "true",
        f"QODER_REALTIME_{region.upper()}_SAT": "fixture_forward_bound_sat",
        f"QODER_REALTIME_{region.upper()}_SA_TEMPLATE_ID": "tmpl_fixture",
    }
    values = realtime_environment(tmp_path / "unused.env", environment, [(region, "sa")])
    assert values[f"QODER_REALTIME_{region.upper()}_SAT"] == "fixture_forward_bound_sat"
