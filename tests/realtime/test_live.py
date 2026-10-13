"""Opt-in CN/Global × PAT/SA × sync/async. Conversations persist; Identities are cleaned."""

from __future__ import annotations

import json
import os
import time
from contextlib import AsyncExitStack, ExitStack
from pathlib import Path
from uuid import uuid4

import httpx
import pytest

from qca import AsyncForward, AsyncServiceAccountCredential, Forward, ServiceAccountCredential
from qca.forward.types.realtime import RealtimeTranscriptPayload
from tests.realtime.config import realtime_environment

pytestmark = pytest.mark.integration


@pytest.fixture(scope="module")
def configuration(request):
    if os.environ.get("QODER_REALTIME_RUN_LIVE") != "1":
        pytest.skip("Set QODER_REALTIME_RUN_LIVE=1 for dedicated Realtime accounts")
    selected = sorted(
        {
            (item.callspec.params["region"], item.callspec.params["auth_mode"])
            for item in request.session.items
            if item.path == Path(__file__).resolve()
        }
    )
    try:
        return realtime_environment(os.environ.get("QODER_LIVE_ENV_FILE", ".env.live"), os.environ, selected)
    except ValueError as exc:
        pytest.fail(str(exc), pytrace=False)


def report(region, auth_mode, phase, **values):
    print(
        json.dumps(
            {"sdk": "python", "region": region, "auth_mode": auth_mode, "phase": phase, **values}, sort_keys=True
        )
    )


def response_report(region, auth_mode, response):
    report(
        region,
        auth_mode,
        "http",
        method=response.request.method,
        path=response.request.url.path,
        status=response.status_code,
        request_id=response.headers.get("x-request-id") or response.headers.get("request-id"),
    )


def sync_flow(client, region, auth_mode, template_id, values):
    identity = client.identities.create(
        external_id=f"sdk-realtime-python-{uuid4().hex}",
        name="SDK Realtime verification",
        enabled=True,
        metadata={"source": "sdk-realtime-test"},
        idempotency_key=uuid4().hex,
    )
    assert identity.id
    report(region, auth_mode, "identity", identity_id=identity.id)
    try:
        conversation = client.realtime.conversations.create(
            identity_id=identity.id,
            template_id=template_id,
            idempotency_key=uuid4().hex,
            title="SDK Realtime verification",
            metadata={"source": "sdk-python-realtime-test"},
        )
        report(region, auth_mode, "conversation", conversation_id=conversation.id, request_id=conversation._request_id)
        with client.realtime.connect(conversation_id=conversation.id) as connection:
            assert connection.ready is not None
            report(region, auth_mode, "ready", conversation_id=conversation.id, request_id=connection.request_id)
            connection.ping()
            seen = []
            for _ in range(100):
                event = connection.recv(timeout=60)
                seen.append(event.type)
                if event.type == "pong":
                    break
            else:
                pytest.fail("No pong received")
            assert "voice.ready" in seen
            pcm_path = (
                values.get(f"QODER_REALTIME_{region.upper()}_PCM_FILE")
                or values.get("QODER_REALTIME_PCM_FILE")
                or values.get("QODER_REALTIME_LIVE_PCM_FILE")
            )
            if pcm_path:
                with Path(pcm_path).open("rb") as stream:
                    while chunk := stream.read(640):
                        connection.append_audio(chunk)
                        time.sleep(0.02)
            else:
                connection.send_text("Please reply with a brief greeting. Do not start a background task.")
            deadline = time.monotonic() + float(values.get("QODER_REALTIME_RESPONSE_TIMEOUT", "120"))
            final = audio_done = audio_received = user_final = False
            while time.monotonic() < deadline and not (
                final and audio_done and audio_received and (user_final or not pcm_path)
            ):
                event = connection.recv(timeout=max(0.001, deadline - time.monotonic()))
                report(
                    region,
                    auth_mode,
                    "event",
                    conversation_id=conversation.id,
                    type=event.type,
                    event_id=event.event_id,
                )
                if (
                    event.type == "transcript.final"
                    and isinstance(event.payload, RealtimeTranscriptPayload)
                    and event.payload.role == "assistant"
                ):
                    assert event.payload.text.strip()
                    final = True
                if (
                    event.type == "transcript.final"
                    and isinstance(event.payload, RealtimeTranscriptPayload)
                    and event.payload.role == "user"
                ):
                    assert event.payload.text.strip()
                    user_final = True
                if event.type == "audio.delta":
                    assert event.audio_bytes()
                    audio_received = True
                if event.type == "audio.done":
                    audio_done = True
                    connection.playback_cancelled(work_id=event.work_id, announcement_id=event.announcement_id)
            assert final and audio_done and audio_received, (
                "Missing assistant transcript.final, non-empty PCM output, or audio.done"
            )
            assert user_final or not pcm_path, "PCM input did not produce a non-empty user transcript.final"
            outcome = connection.close_gracefully()
            report(region, auth_mode, "close", conversation_id=conversation.id, outcome=outcome)
        for kind in ("message", "work", "message,work"):
            page = client.realtime.conversations.history(conversation.id, limit=1, types=kind)
            assert page.conversation.id == conversation.id
            if kind == "message":
                assert page.events, "Saved dialogue history is empty"
                assert all(event.id and event.id.startswith("vevt_") for event in page.events)
            if page.has_next_page():
                older = page.get_next_page()
                assert older.conversation.id == conversation.id
                assert {event.id for event in older.events}.isdisjoint({event.id for event in page.events})
            report(
                region,
                auth_mode,
                "history",
                conversation_id=conversation.id,
                types=kind,
                events=len(page.events),
                has_more=page.page.has_more,
            )
        if auth_mode == "sa" and client.credential is not None:
            with Forward(
                auth_mode="sa", access_token=client.credential.get_token(), base_url=client.base_url, max_retries=0
            ) as direct:
                with direct.realtime.connect(conversation_id=conversation.id) as connection:
                    assert connection.ready is not None
                    connection.ping()
                    for _ in range(100):
                        if connection.recv(timeout=60).type == "pong":
                            break
                    else:
                        pytest.fail("Direct SAT did not receive pong")
                    outcome = connection.close_gracefully()
                    report(region, auth_mode, "direct_sat_close", conversation_id=conversation.id, outcome=outcome)
        return conversation.id
    finally:
        deleted = client.identities.delete(identity.id)
        assert deleted.deleted
        report(region, auth_mode, "cleanup", identity_id=identity.id, deleted=True)


async def async_flow(client, region, auth_mode, template_id, values):
    identity = await client.identities.create(
        external_id=f"sdk-realtime-python-{uuid4().hex}",
        name="SDK Realtime verification",
        enabled=True,
        metadata={"source": "sdk-realtime-test"},
        idempotency_key=uuid4().hex,
    )
    assert identity.id
    report(region, auth_mode, "identity", identity_id=identity.id)
    try:
        conversation = await client.realtime.conversations.create(
            identity_id=identity.id,
            template_id=template_id,
            idempotency_key=uuid4().hex,
            title="SDK Realtime verification",
            metadata={"source": "sdk-python-realtime-test"},
        )
        report(region, auth_mode, "conversation", conversation_id=conversation.id, request_id=conversation._request_id)
        async with await client.realtime.connect(conversation_id=conversation.id) as connection:
            assert connection.ready is not None
            report(region, auth_mode, "ready", conversation_id=conversation.id, request_id=connection.request_id)
            await connection.ping()
            seen = []
            for _ in range(100):
                event = await connection.recv(timeout=60)
                seen.append(event.type)
                if event.type == "pong":
                    break
            else:
                pytest.fail("No pong received")
            assert "voice.ready" in seen
            pcm_path = (
                values.get(f"QODER_REALTIME_{region.upper()}_PCM_FILE")
                or values.get("QODER_REALTIME_PCM_FILE")
                or values.get("QODER_REALTIME_LIVE_PCM_FILE")
            )
            if pcm_path:
                import asyncio

                with Path(pcm_path).open("rb") as stream:
                    while chunk := stream.read(640):
                        await connection.append_audio(chunk)
                        await asyncio.sleep(0.02)
            else:
                await connection.send_text("Please reply with a brief greeting. Do not start a background task.")
            deadline = time.monotonic() + float(values.get("QODER_REALTIME_RESPONSE_TIMEOUT", "120"))
            final = audio_done = audio_received = user_final = False
            while time.monotonic() < deadline and not (
                final and audio_done and audio_received and (user_final or not pcm_path)
            ):
                event = await connection.recv(timeout=max(0.001, deadline - time.monotonic()))
                report(
                    region,
                    auth_mode,
                    "event",
                    conversation_id=conversation.id,
                    type=event.type,
                    event_id=event.event_id,
                )
                if (
                    event.type == "transcript.final"
                    and isinstance(event.payload, RealtimeTranscriptPayload)
                    and event.payload.role == "assistant"
                ):
                    assert event.payload.text.strip()
                    final = True
                if (
                    event.type == "transcript.final"
                    and isinstance(event.payload, RealtimeTranscriptPayload)
                    and event.payload.role == "user"
                ):
                    assert event.payload.text.strip()
                    user_final = True
                if event.type == "audio.delta":
                    assert event.audio_bytes()
                    audio_received = True
                if event.type == "audio.done":
                    audio_done = True
                    await connection.playback_cancelled(work_id=event.work_id, announcement_id=event.announcement_id)
            assert final and audio_done and audio_received, (
                "Missing assistant transcript.final, non-empty PCM output, or audio.done"
            )
            assert user_final or not pcm_path, "PCM input did not produce a non-empty user transcript.final"
            outcome = await connection.close_gracefully()
            report(region, auth_mode, "close", conversation_id=conversation.id, outcome=outcome)
        for kind in ("message", "work", "message,work"):
            page = await client.realtime.conversations.history(conversation.id, limit=1, types=kind)
            assert page.conversation.id == conversation.id
            if kind == "message":
                assert page.events, "Saved dialogue history is empty"
                assert all(event.id and event.id.startswith("vevt_") for event in page.events)
            if page.has_next_page():
                older = await page.get_next_page()
                assert older.conversation.id == conversation.id
                assert {event.id for event in older.events}.isdisjoint({event.id for event in page.events})
            report(
                region,
                auth_mode,
                "history",
                conversation_id=conversation.id,
                types=kind,
                events=len(page.events),
                has_more=page.page.has_more,
            )
        if auth_mode == "sa" and client.credential is not None:
            async with AsyncForward(
                auth_mode="sa",
                access_token=await client.credential.get_token(),
                base_url=client.base_url,
                max_retries=0,
            ) as direct:
                async with await direct.realtime.connect(conversation_id=conversation.id) as connection:
                    assert connection.ready is not None
                    await connection.ping()
                    for _ in range(100):
                        if (await connection.recv(timeout=60)).type == "pong":
                            break
                    else:
                        pytest.fail("Direct SAT did not receive pong")
                    outcome = await connection.close_gracefully()
                    report(region, auth_mode, "direct_sat_close", conversation_id=conversation.id, outcome=outcome)
        return conversation.id
    finally:
        deleted = await client.identities.delete(identity.id)
        assert deleted.deleted
        report(region, auth_mode, "cleanup", identity_id=identity.id, deleted=True)


@pytest.mark.parametrize("region", ["cn", "global"])
@pytest.mark.parametrize("auth_mode", ["pat", "sa"])
def test_sync_realtime(region, auth_mode, configuration):
    values = configuration
    host = "https://api.qoder.com.cn" if region == "cn" else "https://api.qoder.com"
    template = values[f"QODER_REALTIME_{region.upper()}_{auth_mode.upper()}_TEMPLATE_ID"]
    with ExitStack() as stack:
        http = stack.enter_context(
            httpx.Client(
                timeout=30,
                follow_redirects=False,
                event_hooks={"response": [lambda response: response_report(region, auth_mode, response)]},
            )
        )
        options = dict(base_url=f"{host}/api/v1/forward/", max_retries=0, http_client=http)
        if auth_mode == "pat":
            options.update(pat=values[f"QODER_FORWARD_{region.upper()}_PAT"])
        elif values.get(f"QODER_REALTIME_{region.upper()}_SAT", "").strip():
            options.update(auth_mode="sa", access_token=values[f"QODER_REALTIME_{region.upper()}_SAT"])
        else:
            credential = stack.enter_context(
                ServiceAccountCredential(
                    sa_key=values[f"QODER_SA_{region.upper()}_KEY"],
                    region=region,
                    scopes=["qca.access", "forward.access"],
                )
            )
            options.update(auth_mode="sa", credential=credential)
        client = stack.enter_context(Forward(**options))
        sync_flow(client, region, auth_mode, template, values)


@pytest.mark.parametrize("region", ["cn", "global"])
@pytest.mark.parametrize("auth_mode", ["pat", "sa"])
async def test_async_realtime(region, auth_mode, configuration):
    values = configuration
    host = "https://api.qoder.com.cn" if region == "cn" else "https://api.qoder.com"
    template = values[f"QODER_REALTIME_{region.upper()}_{auth_mode.upper()}_TEMPLATE_ID"]

    async def hook(response):
        response_report(region, auth_mode, response)

    async with AsyncExitStack() as stack:
        http = await stack.enter_async_context(
            httpx.AsyncClient(timeout=30, follow_redirects=False, event_hooks={"response": [hook]})
        )
        options = dict(base_url=f"{host}/api/v1/forward/", max_retries=0, http_client=http)
        if auth_mode == "pat":
            options.update(pat=values[f"QODER_FORWARD_{region.upper()}_PAT"])
        elif values.get(f"QODER_REALTIME_{region.upper()}_SAT", "").strip():
            options.update(auth_mode="sa", access_token=values[f"QODER_REALTIME_{region.upper()}_SAT"])
        else:
            credential = await stack.enter_async_context(
                AsyncServiceAccountCredential(
                    sa_key=values[f"QODER_SA_{region.upper()}_KEY"],
                    region=region,
                    scopes=["qca.access", "forward.access"],
                )
            )
            options.update(auth_mode="sa", credential=credential)
        client = await stack.enter_async_context(AsyncForward(**options))
        await async_flow(client, region, auth_mode, template, values)
