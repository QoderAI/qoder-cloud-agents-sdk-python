from __future__ import annotations

import asyncio
import threading
import time
import uuid
from collections import deque
from typing import Any, AsyncIterator, Iterator

from websockets.asyncio.client import ClientConnection as AsyncSocket
from websockets.exceptions import ConnectionClosed, ConnectionClosedOK
from websockets.sync.client import ClientConnection as SyncSocket

from qca.forward.types.realtime import RealtimeClosedPayload, RealtimeErrorPayload, RealtimeEvent, RealtimeReadyPayload

from ._protocol import (
    CLOSE_OUTCOMES,
    TERMINAL_ERRORS,
    RealtimeError,
    RealtimeProtocolError,
    RealtimeQueueOverflowError,
    RealtimeServerError,
    RealtimeTimeoutError,
    encode_event,
    parse_event,
    pcm_payload,
    receipt_payload,
)


class _ConnectionState:
    def __init__(
        self, conversation_id: str, *, max_queue: int, max_queue_bytes: int, send_timeout: float, close_timeout: float
    ) -> None:
        self.conversation_id = conversation_id
        self.ready: RealtimeReadyPayload | None = None
        self.request_id: str | None = None
        self._queue: deque[tuple[RealtimeEvent, int]] = deque()
        self._queue_bytes = 0
        self._max_queue = max_queue
        self._max_queue_bytes = max_queue_bytes
        self._send_timeout = send_timeout
        self._close_timeout = close_timeout
        self._closed = False
        self._closing = False
        self._error: RealtimeError | None = None
        self._close_request_id: str | None = None
        self._close_ack: RealtimeClosedPayload | None = None

    def _accept(self, message: str | bytes) -> None:
        event = parse_event(message, self.conversation_id)
        size = len(message.encode("utf-8")) if isinstance(message, str) else len(message)
        if len(self._queue) >= self._max_queue or self._queue_bytes + size > self._max_queue_bytes:
            raise RealtimeQueueOverflowError(
                "Realtime consumer queue exceeded its budget", conversation_id=self.conversation_id
            )
        self._queue.append((event, size))
        self._queue_bytes += size
        if isinstance(event.payload, RealtimeReadyPayload):
            self.ready = event.payload
        if event.type == "connection.closed" and isinstance(event.payload, RealtimeClosedPayload):
            if event.payload.request_id == self._close_request_id:
                self._close_ack = event.payload
        if event.type == "voice.replaced":
            self._error = RealtimeError("Realtime connection was replaced", conversation_id=self.conversation_id)
            self._closed = True
        if isinstance(event.payload, RealtimeErrorPayload) and event.payload.code in TERMINAL_ERRORS:
            self._error = RealtimeServerError(event)
            self._closed = True

    def _pop(self) -> RealtimeEvent:
        event, size = self._queue.popleft()
        self._queue_bytes -= size
        return event

    def _check_send(self, event_type: str) -> None:
        if self._closed or (self._closing and event_type != "connection.close"):
            raise self._error or RealtimeError(
                "Realtime connection is closed or closing", conversation_id=self.conversation_id
            )
        if self.ready is None:
            raise RealtimeError("Realtime connection is not ready", conversation_id=self.conversation_id)

    def _outcome(self) -> str:
        if self._error:
            raise self._error
        if self._close_ack is None or self._close_ack.outcome not in CLOSE_OUTCOMES:
            raise RealtimeProtocolError(
                "Realtime close did not confirm persistence", conversation_id=self.conversation_id
            )
        return self._close_ack.outcome


class RealtimeConnection(_ConnectionState):
    """Single-reader synchronous voice.realtime.v1 connection with bounded events."""

    def __init__(
        self,
        socket: SyncSocket,
        conversation_id: str,
        *,
        max_queue: int = 256,
        max_queue_bytes: int = 4 * 1024 * 1024,
        send_timeout: float = 30,
        close_timeout: float = 10,
    ) -> None:
        super().__init__(
            conversation_id,
            max_queue=max_queue,
            max_queue_bytes=max_queue_bytes,
            send_timeout=send_timeout,
            close_timeout=close_timeout,
        )
        self._socket = socket
        self.request_id = (
            (socket.response.headers.get("x-request-id") or socket.response.headers.get("request-id"))
            if socket.response
            else None
        )
        self._condition = threading.Condition()
        self._send_lock = threading.Lock()
        self._reader = threading.Thread(target=self._read, name="qca-realtime-reader", daemon=True)
        self._reader.start()

    def _read(self) -> None:
        try:
            while not self._closed:
                message = self._socket.recv()
                with self._condition:
                    self._accept(message)
                    self._condition.notify_all()
        except ConnectionClosedOK:
            pass
        except ConnectionClosed as exc:
            self._error = RealtimeError(
                "Realtime transport closed unexpectedly",
                conversation_id=self.conversation_id,
                close_code=self._socket.close_code,
                close_reason=self._socket.close_reason,
            )
            _ = exc
        except RealtimeError as exc:
            self._error = exc
        except Exception:
            self._error = RealtimeError("Realtime receive failed", conversation_id=self.conversation_id)
        finally:
            with self._condition:
                self._closed = True
                self._condition.notify_all()
            self._socket.close()

    def _wait_ready(self, timeout: float) -> None:
        deadline = time.monotonic() + timeout
        with self._condition:
            while self.ready is None and not self._closed:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise RealtimeTimeoutError("ready", conversation_id=self.conversation_id)
                self._condition.wait(remaining)
            if self._closed:
                raise self._error or RealtimeError("Realtime closed before ready", conversation_id=self.conversation_id)

    def recv(self, *, timeout: float | None = None) -> RealtimeEvent:
        deadline = None if timeout is None else time.monotonic() + timeout
        with self._condition:
            while not self._queue and not self._closed:
                remaining = None if deadline is None else deadline - time.monotonic()
                if remaining is not None and remaining <= 0:
                    raise RealtimeTimeoutError("receive", conversation_id=self.conversation_id)
                self._condition.wait(remaining)
            if self._queue:
                return self._pop()
            if self._error:
                raise self._error
            raise StopIteration

    def __iter__(self) -> Iterator[RealtimeEvent]:
        return self

    def __next__(self) -> RealtimeEvent:
        return self.recv()

    def send_event(self, event_type: str, payload: dict[str, Any] | None = None) -> None:
        message = encode_event(event_type, {} if payload is None else payload)
        deadline = time.monotonic() + self._send_timeout
        if not self._send_lock.acquire(timeout=self._send_timeout):
            raise RealtimeTimeoutError("send", conversation_id=self.conversation_id)
        try:
            self._check_send(event_type)
            done = threading.Event()
            errors: list[Exception] = []

            def send() -> None:
                try:
                    self._socket.send(message)
                except Exception as exc:
                    errors.append(exc)
                finally:
                    done.set()

            writer = threading.Thread(target=send, name="qca-realtime-send", daemon=True)
            writer.start()
            if not done.wait(max(0, deadline - time.monotonic())):
                self._socket.close_socket()
                self.close()
                raise RealtimeTimeoutError("send", conversation_id=self.conversation_id)
            if errors:
                raise RealtimeError("Realtime send failed", conversation_id=self.conversation_id) from errors[0]
        finally:
            self._send_lock.release()

    def send_text(self, text: str) -> None:
        self.send_event("text.message", {"text": text})

    def append_audio(self, pcm_bytes: bytes) -> None:
        self.send_event("audio.append", pcm_payload(pcm_bytes))

    def interrupt(self) -> None:
        self.send_event("interrupt")

    def ping(self) -> None:
        self.send_event("ping")

    def playback_started(self, *, work_id: str | None = None, announcement_id: str | None = None) -> None:
        self.send_event("playback.started", receipt_payload(work_id, announcement_id))

    def playback_ended(self, *, work_id: str | None = None, announcement_id: str | None = None) -> None:
        self.send_event("playback.ended", receipt_payload(work_id, announcement_id))

    def playback_cancelled(self, *, work_id: str | None = None, announcement_id: str | None = None) -> None:
        self.send_event("playback.cancelled", receipt_payload(work_id, announcement_id))

    def close_gracefully(self, *, request_id: str | None = None, timeout: float | None = None) -> str:
        if self.ready is not None and not self.ready.capabilities.graceful_close:
            raise RealtimeError("Server does not support graceful close", conversation_id=self.conversation_id)
        key = uuid.uuid4().hex if request_id is None else request_id
        encode_event("connection.close", {"request_id": key})
        if self._closing:
            raise RealtimeError("Realtime graceful close is already in progress", conversation_id=self.conversation_id)
        self._closing = True
        self._close_request_id = key
        deadline = time.monotonic() + (self._close_timeout if timeout is None else timeout)
        try:
            self.send_event("connection.close", {"request_id": key})
            with self._condition:
                while self._close_ack is None and not self._closed:
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        raise RealtimeTimeoutError("graceful close", conversation_id=self.conversation_id)
                    self._condition.wait(remaining)
                return self._outcome()
        finally:
            self.close()

    def close(self) -> None:
        with self._condition:
            self._closed = True
            self._condition.notify_all()
        self._socket.close()
        if threading.current_thread() is not self._reader:
            self._reader.join(timeout=self._close_timeout + 1)

    def __enter__(self) -> RealtimeConnection:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


class AsyncRealtimeConnection(_ConnectionState):
    """Async connection; only its background task reads WebSocket messages."""

    def __init__(
        self,
        socket: AsyncSocket,
        conversation_id: str,
        *,
        max_queue: int = 256,
        max_queue_bytes: int = 4 * 1024 * 1024,
        send_timeout: float = 30,
        close_timeout: float = 10,
    ) -> None:
        super().__init__(
            conversation_id,
            max_queue=max_queue,
            max_queue_bytes=max_queue_bytes,
            send_timeout=send_timeout,
            close_timeout=close_timeout,
        )
        self._socket = socket
        self.request_id = (
            (socket.response.headers.get("x-request-id") or socket.response.headers.get("request-id"))
            if socket.response
            else None
        )
        self._condition = asyncio.Condition()
        self._send_lock = asyncio.Lock()
        self._reader = asyncio.create_task(self._read(), name="qca-realtime-reader")

    async def _read(self) -> None:
        try:
            while not self._closed:
                message = await self._socket.recv()
                async with self._condition:
                    self._accept(message)
                    self._condition.notify_all()
        except ConnectionClosedOK:
            pass
        except ConnectionClosed:
            self._error = RealtimeError(
                "Realtime transport closed unexpectedly",
                conversation_id=self.conversation_id,
                close_code=self._socket.close_code,
                close_reason=self._socket.close_reason,
            )
        except RealtimeError as exc:
            self._error = exc
        except asyncio.CancelledError:
            raise
        except Exception:
            self._error = RealtimeError("Realtime receive failed", conversation_id=self.conversation_id)
        finally:
            async with self._condition:
                self._closed = True
                self._condition.notify_all()
            await self._socket.close()

    async def _wait_ready(self, timeout: float) -> None:
        async def wait() -> None:
            async with self._condition:
                while self.ready is None and not self._closed:
                    await self._condition.wait()
                if self._closed:
                    raise self._error or RealtimeError(
                        "Realtime closed before ready", conversation_id=self.conversation_id
                    )

        try:
            await asyncio.wait_for(wait(), timeout)
        except asyncio.TimeoutError as exc:
            raise RealtimeTimeoutError("ready", conversation_id=self.conversation_id) from exc

    async def recv(self, *, timeout: float | None = None) -> RealtimeEvent:
        async def wait() -> RealtimeEvent:
            async with self._condition:
                while not self._queue and not self._closed:
                    await self._condition.wait()
                if self._queue:
                    return self._pop()
                if self._error:
                    raise self._error
                raise StopAsyncIteration

        try:
            return await asyncio.wait_for(wait(), timeout)
        except asyncio.TimeoutError as exc:
            raise RealtimeTimeoutError("receive", conversation_id=self.conversation_id) from exc

    def __aiter__(self) -> AsyncIterator[RealtimeEvent]:
        return self

    async def __anext__(self) -> RealtimeEvent:
        return await self.recv()

    async def send_event(self, event_type: str, payload: dict[str, Any] | None = None) -> None:
        message = encode_event(event_type, {} if payload is None else payload)

        async def send() -> None:
            async with self._send_lock:
                self._check_send(event_type)
                await self._socket.send(message)

        try:
            await asyncio.wait_for(send(), self._send_timeout)
        except asyncio.TimeoutError as exc:
            await self.close()
            raise RealtimeTimeoutError("send", conversation_id=self.conversation_id) from exc
        except ConnectionClosed as exc:
            raise RealtimeError("Realtime send failed", conversation_id=self.conversation_id) from exc

    async def send_text(self, text: str) -> None:
        await self.send_event("text.message", {"text": text})

    async def append_audio(self, pcm_bytes: bytes) -> None:
        await self.send_event("audio.append", pcm_payload(pcm_bytes))

    async def interrupt(self) -> None:
        await self.send_event("interrupt")

    async def ping(self) -> None:
        await self.send_event("ping")

    async def playback_started(self, *, work_id: str | None = None, announcement_id: str | None = None) -> None:
        await self.send_event("playback.started", receipt_payload(work_id, announcement_id))

    async def playback_ended(self, *, work_id: str | None = None, announcement_id: str | None = None) -> None:
        await self.send_event("playback.ended", receipt_payload(work_id, announcement_id))

    async def playback_cancelled(self, *, work_id: str | None = None, announcement_id: str | None = None) -> None:
        await self.send_event("playback.cancelled", receipt_payload(work_id, announcement_id))

    async def close_gracefully(self, *, request_id: str | None = None, timeout: float | None = None) -> str:
        if self.ready is not None and not self.ready.capabilities.graceful_close:
            raise RealtimeError("Server does not support graceful close", conversation_id=self.conversation_id)
        key = uuid.uuid4().hex if request_id is None else request_id
        encode_event("connection.close", {"request_id": key})
        if self._closing:
            raise RealtimeError("Realtime graceful close is already in progress", conversation_id=self.conversation_id)
        self._closing = True
        self._close_request_id = key

        async def wait() -> str:
            async with self._condition:
                while self._close_ack is None and not self._closed:
                    await self._condition.wait()
                return self._outcome()

        try:
            await self.send_event("connection.close", {"request_id": key})
            try:
                return await asyncio.wait_for(wait(), self._close_timeout if timeout is None else timeout)
            except asyncio.TimeoutError as exc:
                raise RealtimeTimeoutError("graceful close", conversation_id=self.conversation_id) from exc
        finally:
            await self.close()

    async def close(self) -> None:
        async with self._condition:
            self._closed = True
            self._condition.notify_all()
        await self._socket.close()
        if asyncio.current_task() is not self._reader:
            if not self._reader.done():
                self._reader.cancel()
            await asyncio.gather(self._reader, return_exceptions=True)

    async def __aenter__(self) -> AsyncRealtimeConnection:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.close()
