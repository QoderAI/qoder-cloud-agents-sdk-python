"""Server-sent events: framing, checkpoints and connection release.

The first tests pin the decoder against hand-written wire bytes. The last one
replays every ending an SSE call can hit against all four streaming endpoints,
because leaking a response there leaves a socket open for the caller.
"""

import asyncio

import httpx
import pytest

from qca import (
    APIConnectionError,
    APIError,
    APIResponseValidationError,
    APITimeoutError,
    AsyncManaged,
    Forward,
)

from ._surface import ENDPOINTS, call, client_for, close_client, endpoint_id

STREAMS = [endpoint for endpoint in ENDPOINTS if endpoint.kind == "stream"]


class Chunks(httpx.SyncByteStream):
    """Delivers the body in three-byte pieces, splitting frames mid-field."""

    closed = False

    def __init__(self, content):
        self.content = content

    def __iter__(self):
        for index in range(0, len(self.content), 3):
            yield self.content[index : index + 3]

    def close(self):
        self.closed = True


def test_sse_multiline_utf8_comments_deltas_and_checkpoint():
    body = (
        ": keepalive\r\n\r\n"
        'id: one\r\nevent: agent.message\r\ndata: {"content":\r\ndata: [{"type":"text","text":"你好"}]}\r\n\r\n'
        'id: two\nevent: event_delta\ndata: {"text":"a"}\n\n'
        'id: two\nevent: event_delta\ndata: {"text":"b"}\n\n'
        'id: incomplete\ndata: {"text":"never emit"}'
    ).encode()
    chunks = Chunks(body)

    def handle(request):
        assert request.headers["Last-Event-ID"] == "previous"
        assert request.headers["Accept"] == "text/event-stream"
        assert request.url.params.get_list("event_deltas[]") == ["agent.message"]
        return httpx.Response(200, stream=chunks, headers={"content-type": "text/event-stream"})

    with Forward(pat="test", http_client=httpx.Client(transport=httpx.MockTransport(handle))) as client:
        with client.sessions.events.stream(
            "session", last_event_id="previous", event_deltas=["agent.message"]
        ) as stream:
            events = list(stream)
            assert [event.type for event in events] == ["agent.message", "event_delta", "event_delta"]
            assert events[0].content[0]["text"] == "你好"
            assert stream.last_event_id == "two"
    assert chunks.closed


@pytest.mark.parametrize(
    "body,error",
    [
        ('event: error\ndata: {"error":{"message":"stream error"}}\n\n', APIError),
        ("data: invalid json\n\n", APIResponseValidationError),
    ],
    ids=["remote_error", "invalid_json"],
)
def test_stream_errors_close_response(body, error):
    chunks = Chunks(body.encode())
    with Forward(
        pat="test",
        http_client=httpx.Client(transport=httpx.MockTransport(lambda _: httpx.Response(200, stream=chunks)))
    ) as client:
        with pytest.raises(error):
            list(client.sessions.events.stream("session"))
    assert chunks.closed


async def test_async_stream_is_incremental_and_context_closes_on_break():
    class AsyncChunks(httpx.AsyncByteStream):
        closed = False

        async def __aiter__(self):
            yield b'id: evt\nevent: agent.message\ndata: {"content":[{"type":"text","text":"hello"}]}\n\n'
            await asyncio.Event().wait()

        async def aclose(self):
            self.closed = True

    chunks = AsyncChunks()
    async with AsyncManaged(
        pat="test",
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(lambda _: httpx.Response(200, stream=chunks)))
    ) as client:
        async with await client.sessions.events.stream("session", extra_headers={"Last-Event-ID": "before"}) as stream:
            async for event in stream:
                assert event.content[0].text == "hello"
                break
            assert stream.last_event_id == "evt"
    assert chunks.closed


@pytest.mark.parametrize("endpoint", STREAMS, ids=endpoint_id)
@pytest.mark.parametrize("async_", [False, True], ids=["sync", "async"])
@pytest.mark.parametrize("ending", ["done", "invalid_json", "remote_error", "timeout", "disconnect"])
async def test_each_sse_api_closes_and_keeps_its_last_checkpoint(endpoint, async_, ending):
    class EventBytes(httpx.SyncByteStream, httpx.AsyncByteStream):
        closed = False

        def __iter__(self):
            first = 'id: first\nevent: agent.message\ndata: {"content":[{"type":"text","text":"你好"}]}\n\n'.encode()
            for index in range(0, len(first), 3):
                yield first[index : index + 3]
            yield b"id: ignored\nevent: ping\ndata: {}\n\n"
            if ending == "timeout":
                raise httpx.ReadTimeout("stream timed out")
            if ending == "disconnect":
                raise httpx.ReadError("stream disconnected")
            yield {
                "done": b"data: [DONE]\n\n",
                "invalid_json": b"id: invalid\ndata: {broken\n\n",
                "remote_error": b'id: failed\nevent: error\ndata: {"error":{"message":"remote failure"}}\n\n',
            }[ending]

        async def __aiter__(self):
            for chunk in self:
                yield chunk

        def close(self):
            self.closed = True

        async def aclose(self):
            self.closed = True

    body = EventBytes()
    client = client_for(
        endpoint,
        async_,
        lambda _: httpx.Response(200, stream=body, headers={"content-type": "text/event-stream"}),
    )
    try:
        stream = await call(endpoint, client)
        first = await anext(stream) if async_ else next(stream)
        assert (first.id, first.type) == ("first", "agent.message")
        if ending == "done":
            with pytest.raises(StopAsyncIteration if async_ else StopIteration):
                await anext(stream) if async_ else next(stream)
        else:
            expected = {
                "invalid_json": APIResponseValidationError,
                "remote_error": APIError,
                "timeout": APITimeoutError,
                "disconnect": APIConnectionError,
            }[ending]
            with pytest.raises(expected):
                await anext(stream) if async_ else next(stream)
        # The ping frame carries an id but no payload, so it must not move the checkpoint.
        assert stream.last_event_id == "first"
        assert body.closed and stream.response.is_closed
    finally:
        await close_client(client, async_)
