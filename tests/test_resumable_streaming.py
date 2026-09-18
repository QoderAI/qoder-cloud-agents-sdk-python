import asyncio
import threading
from collections.abc import Iterator
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from types import SimpleNamespace
from typing import Any

import httpx
import pytest

from qca import AsyncForward, AsyncManaged, ConflictError, Forward, Managed
from qca.common._resumable_streaming import AsyncResumableStream, ResumableStream

CLIENTS = {
    ("forward", False): Forward,
    ("forward", True): AsyncForward,
    ("managed", False): Managed,
    ("managed", True): AsyncManaged,
}

_FIRST_EVENT = b'id: evt-1\nevent: event_delta\ndata: {"text":"first"}\n\n'
_TERMINAL_EVENT = b'id: evt-2\nevent: session.status_terminated\ndata: {"type":"session.status_terminated"}\n\n'


@contextmanager
def run_abrupt_sse_server() -> Iterator[tuple[str, list[dict[str, str | None]]]]:
    requests: list[dict[str, str | None]] = []

    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def do_GET(self) -> None:
            requests.append({"path": self.path, "last_event_id": self.headers.get("Last-Event-ID")})
            body = _FIRST_EVENT if len(requests) == 1 else _TERMINAL_EVENT
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Connection", "close")
            self.send_header("Content-Length", str(len(body) + (64 if len(requests) == 1 else 0)))
            self.end_headers()
            self.wfile.write(body)
            self.wfile.flush()
            self.close_connection = True

        def log_message(self, _format: str, *args: Any) -> None:
            pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever)
    thread.start()
    try:
        host, port = server.server_address
        yield f"http://{host}:{port}", requests
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)
        assert not thread.is_alive()


class ScriptedBody(httpx.SyncByteStream, httpx.AsyncByteStream):
    def __init__(self, content: bytes, *, disconnect: bool = False) -> None:
        self.content = content
        self.disconnect = disconnect
        self.closed = False

    def __iter__(self):
        yield self.content
        if self.disconnect:
            raise httpx.ReadError("disconnected")

    async def __aiter__(self):
        for chunk in self:
            yield chunk

    def close(self) -> None:
        self.closed = True

    async def aclose(self) -> None:
        self.closed = True


def make_client(mode: str, async_: bool, handler: Any):
    transport = httpx.MockTransport(handler)
    http_client = httpx.AsyncClient(transport=transport) if async_ else httpx.Client(transport=transport)
    return CLIENTS[mode, async_](
        pat="test",
        base_url=f"https://api.test/api/v1/{mode}",
        max_retries=0,
        http_client=http_client,
    )


async def close_client(client: Any, async_: bool) -> None:
    if async_:
        await client.close()
    else:
        client.close()


@pytest.mark.parametrize("mode", ["forward", "managed"])
@pytest.mark.parametrize("async_", [False, True], ids=["sync", "async"])
async def test_resumable_stream_reconnects_over_real_http(monkeypatch, mode, async_):
    monkeypatch.setattr("qca.common._resumable_streaming.random.uniform", lambda *_: 0)
    prefix = "forward" if mode == "forward" else "cloud"

    with run_abrupt_sse_server() as (server_url, requests):
        http_client = httpx.AsyncClient(trust_env=False) if async_ else httpx.Client(trust_env=False)
        client = CLIENTS[mode, async_](
            pat="test",
            base_url=f"{server_url}/api/v1/{prefix}",
            max_retries=0,
            http_client=http_client,
        )
        stream = client.sessions.events.resumable_stream("session")
        try:
            if async_:
                events = [await anext(stream), await anext(stream)]
                with pytest.raises(StopAsyncIteration):
                    await anext(stream)
            else:
                events = [next(stream), next(stream)]
                with pytest.raises(StopIteration):
                    next(stream)

            assert [event.id for event in events] == ["evt-1", "evt-2"]
            assert [event.type for event in events] == ["event_delta", "session.status_terminated"]
            assert stream.last_event_id == "evt-2"
            path = f"/api/v1/{prefix}/sessions/session/events/stream"
            assert requests == [
                {"path": path, "last_event_id": None},
                {"path": path, "last_event_id": "evt-1"},
            ]
        finally:
            if async_:
                await stream.close()
            else:
                stream.close()
            await close_client(client, async_)


@pytest.mark.parametrize("mode", ["forward", "managed"])
@pytest.mark.parametrize("async_", [False, True], ids=["sync", "async"])
@pytest.mark.parametrize("ending", ["eof", "transport"])
async def test_resumable_stream_reconnects_with_checkpoint_and_preserves_params(monkeypatch, mode, async_, ending):
    monkeypatch.setattr("qca.common._resumable_streaming.random.uniform", lambda *_: 0)
    requests = []
    bodies = []

    first = (
        'id: preview\nevent: event_delta\ndata: {"text":"a"}\n\n'
        'id: preview\nevent: event_delta\ndata: {"text":"b"}\n\n'
        'id: partial\nevent: event_delta\ndata: {"text":"never delivered"}'
    ).encode()
    second = b'id: final\nevent: event_delta\ndata: {"text":"c"}\n\n'

    def handle(request):
        requests.append(request)
        attempt = len(requests)
        assert request.url.params.get_list("event_deltas[]") == ["agent.message", "agent.thinking"]
        assert request.url.params["trace"] == "kept"
        assert request.headers["x-test"] == "kept"
        assert request.extensions["timeout"]["read"] == 7
        if mode == "forward":
            assert request.url.params["include_tool_calls"] == "false"
            assert request.url.params["include_thinking"] == "true"
        else:
            assert request.headers["qoder-workspace-id"] == "workspace"
            assert request.headers["x-qoder-beta"] == "beta-1,beta-2"
        assert request.headers["last-event-id"] == ("initial" if attempt == 1 else "preview")
        body = ScriptedBody(first if attempt == 1 else second, disconnect=attempt == 1 and ending == "transport")
        bodies.append(body)
        return httpx.Response(200, stream=body, headers={"content-type": "text/event-stream"})

    client = make_client(mode, async_, handle)
    kwargs = {
        "event_deltas": ["agent.message", "agent.thinking"],
        "last_event_id": "initial",
        "extra_headers": {"X-Test": "kept"},
        "extra_query": {"trace": "kept"},
        "extra_body": {"ignored-by-get": True},
        "timeout": 7,
    }
    if mode == "forward":
        kwargs.update(include_tool_calls=False, include_thinking=True)
    else:
        kwargs.update(workspace_id="workspace", betas=["beta-1", "beta-2"])

    stream = client.sessions.events.resumable_stream("session", **kwargs)
    try:
        if async_:
            events = [await anext(stream), await anext(stream), await anext(stream)]
            await stream.close()
        else:
            events = [next(stream), next(stream), next(stream)]
            stream.close()
        assert [event.id for event in events] == ["preview", "preview", "final"]
        assert [event.text for event in events] == ["a", "b", "c"]
        assert stream.last_event_id == "final"
        assert len(requests) == 2
        assert all(body.closed for body in bodies)
    finally:
        await close_client(client, async_)


@pytest.mark.parametrize("mode", ["forward", "managed"])
@pytest.mark.parametrize("async_", [False, True], ids=["sync", "async"])
@pytest.mark.parametrize(
    ("initial_cursor", "bodies", "expected_headers", "expected_checkpoint"),
    [
        (
            "initial",
            [
                b'event: event_delta\ndata: {"text":"without id"}\n\n',
                b'event: session.status_terminated\ndata: {"type":"session.status_terminated"}\n\n',
            ],
            ["initial", "initial"],
            "initial",
        ),
        (
            "initial",
            [
                b'id: prior\nevent: event_delta\ndata: {"text":"checkpointed"}\n\n',
                b'event: event_delta\ndata: {"text":"without id"}\n\n',
                b'event: session.status_terminated\ndata: {"type":"session.status_terminated"}\n\n',
            ],
            ["initial", "prior", "prior"],
            "prior",
        ),
        (
            "",
            [
                b'event: event_delta\ndata: {"text":"without id"}\n\n',
                b'event: session.status_terminated\ndata: {"type":"session.status_terminated"}\n\n',
            ],
            ["", ""],
            "",
        ),
    ],
    ids=["initial", "prior", "empty"],
)
async def test_resumable_stream_keeps_checkpoint_across_idless_event(
    monkeypatch, mode, async_, initial_cursor, bodies, expected_headers, expected_checkpoint
):
    monkeypatch.setattr("qca.common._resumable_streaming.random.uniform", lambda *_: 0)
    requests = []

    def handle(request):
        requests.append(request)
        index = len(requests) - 1
        assert request.headers["last-event-id"] == expected_headers[index]
        return httpx.Response(200, content=bodies[index], headers={"content-type": "text/event-stream"})

    client = make_client(mode, async_, handle)
    stream = client.sessions.events.resumable_stream("session", last_event_id=initial_cursor)
    try:
        if async_:
            events = [await anext(stream) for _ in bodies]
            with pytest.raises(StopAsyncIteration):
                await anext(stream)
        else:
            events = [next(stream) for _ in bodies]
            with pytest.raises(StopIteration):
                next(stream)
        assert [event.type for event in events[-2:]] == ["event_delta", "session.status_terminated"]
        assert stream.last_event_id == expected_checkpoint
        assert len(requests) == len(expected_headers)
    finally:
        if async_:
            await stream.close()
        else:
            stream.close()
        await close_client(client, async_)


@pytest.mark.parametrize("mode", ["forward", "managed"])
@pytest.mark.parametrize("async_", [False, True], ids=["sync", "async"])
async def test_resumable_stream_does_not_retry_409(mode, async_):
    requests = []

    def handle(request):
        requests.append(request)
        return httpx.Response(
            409,
            json={"error": {"message": "invalid cursor"}},
            headers={"x-should-retry": "true"},
        )

    client = make_client(mode, async_, handle)
    stream = client.sessions.events.resumable_stream("session", last_event_id="invalid")
    try:
        with pytest.raises(ConflictError):
            if async_:
                await anext(stream)
            else:
                next(stream)
        assert len(requests) == 1
    finally:
        if async_:
            await stream.close()
        else:
            stream.close()
        await close_client(client, async_)


@pytest.mark.parametrize("mode", ["forward", "managed"])
def test_sync_resumable_stream_close_interrupts_active_read(mode):
    class HangingBody(httpx.SyncByteStream):
        def __init__(self) -> None:
            self.started = threading.Event()
            self.released = threading.Event()
            self.closed = False

        def __iter__(self):
            self.started.set()
            self.released.wait()
            return
            yield b""  # pragma: no cover

        def close(self) -> None:
            self.closed = True
            self.released.set()

    body = HangingBody()
    client = make_client(mode, False, lambda _: httpx.Response(200, stream=body))
    stream = client.sessions.events.resumable_stream("session")
    try:
        with ThreadPoolExecutor(max_workers=1) as executor:
            pending = executor.submit(next, stream)
            assert body.started.wait(timeout=1)
            stream.close()
            with pytest.raises(StopIteration):
                pending.result(timeout=1)
        assert body.closed
    finally:
        client.close()


@pytest.mark.parametrize("mode", ["forward", "managed"])
async def test_async_resumable_stream_close_interrupts_active_read_and_is_idempotent(mode):
    class HangingBody(httpx.AsyncByteStream):
        def __init__(self) -> None:
            self.started = asyncio.Event()
            self.released = asyncio.Event()
            self.close_calls = 0

        async def __aiter__(self):
            self.started.set()
            await self.released.wait()
            return
            yield b""  # pragma: no cover

        async def aclose(self) -> None:
            self.close_calls += 1
            self.released.set()

    body = HangingBody()
    client = make_client(mode, True, lambda _: httpx.Response(200, stream=body))
    stream = client.sessions.events.resumable_stream("session")
    pending = asyncio.create_task(anext(stream))
    try:
        await asyncio.wait_for(body.started.wait(), timeout=1)
        await asyncio.wait_for(stream.close(), timeout=1)
        await asyncio.wait_for(stream.close(), timeout=1)
        with pytest.raises(StopAsyncIteration):
            await asyncio.wait_for(pending, timeout=1)
        assert body.close_calls == 1
    finally:
        await stream.close()
        await client.close()


@pytest.mark.parametrize("mode", ["forward", "managed"])
async def test_async_resumable_stream_cancellation_closes_active_read(mode):
    class HangingBody(httpx.AsyncByteStream):
        def __init__(self) -> None:
            self.started = asyncio.Event()
            self.closed = False

        async def __aiter__(self):
            self.started.set()
            await asyncio.Event().wait()
            yield b""  # pragma: no cover

        async def aclose(self) -> None:
            self.closed = True

    body = HangingBody()
    client = make_client(mode, True, lambda _: httpx.Response(200, stream=body))
    stream = client.sessions.events.resumable_stream("session")
    pending = asyncio.create_task(anext(stream))
    try:
        await asyncio.wait_for(body.started.wait(), timeout=1)
        pending.cancel()
        with pytest.raises(asyncio.CancelledError):
            await pending
        assert body.closed
    finally:
        await stream.close()
        await client.close()


@pytest.mark.parametrize("mode", ["forward", "managed"])
@pytest.mark.parametrize("async_", [False, True], ids=["sync", "async"])
@pytest.mark.parametrize("terminal_type", ["session.status_terminated", "session.deleted"])
async def test_terminal_event_stops_reconnection(mode, async_, terminal_type):
    requests = []

    def handle(request):
        requests.append(request)
        body = f'id: terminal\nevent: {terminal_type}\ndata: {{"type":"{terminal_type}"}}\n\n'.encode()
        return httpx.Response(200, content=body, headers={"content-type": "text/event-stream"})

    client = make_client(mode, async_, handle)
    stream = client.sessions.events.resumable_stream("session")
    try:
        if async_:
            event = await anext(stream)
            with pytest.raises(StopAsyncIteration):
                await anext(stream)
        else:
            event = next(stream)
            with pytest.raises(StopIteration):
                next(stream)
        assert event.type == terminal_type
        assert stream.last_event_id == "terminal"
        assert len(requests) == 1
    finally:
        if async_:
            await stream.close()
        else:
            stream.close()
        await close_client(client, async_)


async def test_async_resumable_stream_close_interrupts_active_open_and_is_idempotent():
    started = asyncio.Event()
    cancelled = asyncio.Event()

    async def open_stream(_: str | None):
        started.set()
        try:
            await asyncio.Event().wait()
        finally:
            cancelled.set()

    stream = AsyncResumableStream(open_stream=open_stream, retryable=lambda *_: True, last_event_id=None)
    pending = asyncio.create_task(anext(stream))
    await asyncio.wait_for(started.wait(), timeout=1)

    await asyncio.wait_for(stream.close(), timeout=1)
    await asyncio.wait_for(stream.close(), timeout=1)

    with pytest.raises(StopAsyncIteration):
        await asyncio.wait_for(pending, timeout=1)
    assert cancelled.is_set()


class _ScriptedSyncStream:
    def __init__(self, events):
        self._events = iter(events)
        self.last_event_id = None

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._events)

    def close(self):
        pass


class _ScriptedAsyncStream:
    def __init__(self, events):
        self._events = iter(events)
        self.last_event_id = None

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            return next(self._events)
        except StopIteration:
            raise StopAsyncIteration from None

    async def close(self):
        pass


@pytest.mark.parametrize(
    ("connected_times", "expected_backoffs"),
    [
        ([0.0, 1.0, 2.0, 3.0, 4.0, 4.0], [0.5, 1.0]),
        ([0.0, 1.0, 2.0, 8.0, 9.0, 9.0], [0.5, 0.5]),
    ],
    ids=["event-does-not-reset-short-connection", "healthy-connection-resets"],
)
def test_sync_resumable_stream_resets_backoff_only_after_healthy_connection(
    monkeypatch, connected_times, expected_backoffs
):
    times = iter(connected_times)
    backoffs = []
    attempts = 0
    stream = None

    def open_stream(_: str | None):
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            return _ScriptedSyncStream([])
        if attempts == 2:
            return _ScriptedSyncStream([SimpleNamespace(type="agent.message")])
        assert stream is not None
        stream.close()
        return _ScriptedSyncStream([])

    def record_backoff(_lower, upper):
        backoffs.append(upper)
        return 0

    monkeypatch.setattr("qca.common._resumable_streaming.monotonic", lambda: next(times))
    monkeypatch.setattr("qca.common._resumable_streaming.random.uniform", record_backoff)
    stream = ResumableStream(open_stream=open_stream, retryable=lambda *_: True, last_event_id=None)

    assert next(stream).type == "agent.message"
    with pytest.raises(StopIteration):
        next(stream)
    assert backoffs == expected_backoffs


@pytest.mark.parametrize(
    ("connected_times", "expected_backoffs"),
    [
        ([0.0, 1.0, 2.0, 3.0, 4.0, 4.0], [0.5, 1.0]),
        ([0.0, 1.0, 2.0, 8.0, 9.0, 9.0], [0.5, 0.5]),
    ],
    ids=["event-does-not-reset-short-connection", "healthy-connection-resets"],
)
async def test_async_resumable_stream_resets_backoff_only_after_healthy_connection(
    monkeypatch, connected_times, expected_backoffs
):
    times = iter(connected_times)
    backoffs = []
    attempts = 0
    stream = None

    async def open_stream(_: str | None):
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            return _ScriptedAsyncStream([])
        if attempts == 2:
            return _ScriptedAsyncStream([SimpleNamespace(type="agent.message")])
        assert stream is not None
        await stream.close()
        return _ScriptedAsyncStream([])

    def record_backoff(_lower, upper):
        backoffs.append(upper)
        return 0

    monkeypatch.setattr("qca.common._resumable_streaming.monotonic", lambda: next(times))
    monkeypatch.setattr("qca.common._resumable_streaming.random.uniform", record_backoff)
    stream = AsyncResumableStream(open_stream=open_stream, retryable=lambda *_: True, last_event_id=None)

    assert (await anext(stream)).type == "agent.message"
    with pytest.raises(StopAsyncIteration):
        await anext(stream)
    assert backoffs == expected_backoffs
