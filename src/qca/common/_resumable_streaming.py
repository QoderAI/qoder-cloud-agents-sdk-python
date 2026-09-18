from __future__ import annotations

import random
import threading
from collections.abc import AsyncIterator, Awaitable, Callable, Iterator
from time import monotonic
from typing import Generic, TypeVar

import anyio
import httpx

from ._exceptions import APIConnectionError, APIStatusError
from ._streaming import AsyncStream, Stream

T = TypeVar("T")

_INITIAL_BACKOFF = 0.5
_MAX_BACKOFF = 10.0
_HEALTHY_RESET_AFTER = 5.0
_TERMINAL_EVENT_TYPES = frozenset({"session.status_terminated", "session.deleted"})

Retryable = Callable[[httpx.Request, httpx.Response | None], bool]


def _is_terminal_event(event: object) -> bool:
    return getattr(event, "type", None) in _TERMINAL_EVENT_TYPES


class ResumableStream(Generic[T], Iterator[T]):
    def __init__(
        self,
        *,
        open_stream: Callable[[str | None], Stream[T]],
        retryable: Retryable,
        last_event_id: str | None,
    ) -> None:
        self._open_stream = open_stream
        self._retryable = retryable
        self._last_event_id = last_event_id
        self._backoff = _INITIAL_BACKOFF
        self._closed = threading.Event()
        self._stream: Stream[T] | None = None
        self._iterator = self._iter_events()

    @property
    def last_event_id(self) -> str | None:
        return self._last_event_id

    def __next__(self) -> T:
        return next(self._iterator)

    def _iter_events(self) -> Iterator[T]:
        while not self._closed.is_set():
            connected_at: float | None = None
            connected_for: float | None = None
            stream: Stream[T] | None = None
            try:
                stream = self._open_stream(self._last_event_id)
                self._stream = stream
                connected_at = monotonic()
                if self._closed.is_set():
                    return
                for event in stream:
                    if self._closed.is_set():
                        return
                    if stream.last_event_id:
                        self._last_event_id = stream.last_event_id
                    terminal = _is_terminal_event(event)
                    yield event
                    if terminal:
                        return
            except APIConnectionError as exc:
                if self._closed.is_set():
                    return
                if not self._retryable(exc.request, None):
                    raise
            except APIStatusError as exc:
                if self._closed.is_set():
                    return
                if not self._retryable(exc.request, exc.response):
                    raise
            finally:
                if connected_at is not None:
                    connected_for = monotonic() - connected_at
                if stream is not None:
                    stream.close()
                self._stream = None

            if self._closed.is_set():
                return
            if connected_for is not None and connected_for >= _HEALTHY_RESET_AFTER:
                self._backoff = _INITIAL_BACKOFF
            delay = random.uniform(self._backoff / 2, self._backoff)
            self._backoff = min(self._backoff * 2, _MAX_BACKOFF)
            if self._closed.wait(delay):
                return

    def close(self) -> None:
        self._closed.set()
        if self._stream is not None:
            self._stream.close()

    def __enter__(self) -> ResumableStream[T]:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


class AsyncResumableStream(Generic[T], AsyncIterator[T]):
    def __init__(
        self,
        *,
        open_stream: Callable[[str | None], Awaitable[AsyncStream[T]]],
        retryable: Retryable,
        last_event_id: str | None,
    ) -> None:
        self._open_stream = open_stream
        self._retryable = retryable
        self._last_event_id = last_event_id
        self._backoff = _INITIAL_BACKOFF
        self._closed = False
        self._close_event: anyio.Event | None = None
        self._cancel_scope: anyio.CancelScope | None = None
        self._stream: AsyncStream[T] | None = None
        self._iterator = self._iter_events()

    @property
    def last_event_id(self) -> str | None:
        return self._last_event_id

    async def __anext__(self) -> T:
        return await self._iterator.__anext__()

    async def _open_next_stream(self) -> AsyncStream[T] | None:
        stream: AsyncStream[T] | None = None
        with anyio.CancelScope() as cancel_scope:
            self._cancel_scope = cancel_scope
            if self._closed:
                cancel_scope.cancel()
            try:
                stream = await self._open_stream(self._last_event_id)
            finally:
                if self._cancel_scope is cancel_scope:
                    self._cancel_scope = None
        return stream

    async def _next_event(self, stream: AsyncStream[T]) -> tuple[bool, T | None]:
        event: T | None = None
        exhausted = False
        with anyio.CancelScope() as cancel_scope:
            self._cancel_scope = cancel_scope
            if self._closed:
                cancel_scope.cancel()
            try:
                event = await stream.__anext__()
            except StopAsyncIteration:
                exhausted = True
            finally:
                if self._cancel_scope is cancel_scope:
                    self._cancel_scope = None
        return exhausted, event

    async def _close_stream(self, stream: AsyncStream[T]) -> None:
        if self._stream is not stream:
            return
        self._stream = None
        await stream.close()

    async def _iter_events(self) -> AsyncIterator[T]:
        while not self._closed:
            connected_at: float | None = None
            connected_for: float | None = None
            stream: AsyncStream[T] | None = None
            try:
                stream = await self._open_next_stream()
                if stream is None:
                    return
                self._stream = stream
                connected_at = monotonic()
                if self._closed:
                    return
                while not self._closed:
                    exhausted, event = await self._next_event(stream)
                    if self._closed:
                        return
                    if exhausted:
                        break
                    if event is None:
                        raise RuntimeError("stream read was interrupted without closing")
                    if stream.last_event_id:
                        self._last_event_id = stream.last_event_id
                    terminal = _is_terminal_event(event)
                    yield event
                    if terminal:
                        return
            except APIConnectionError as exc:
                if self._closed:
                    return
                if not self._retryable(exc.request, None):
                    raise
            except APIStatusError as exc:
                if self._closed:
                    return
                if not self._retryable(exc.request, exc.response):
                    raise
            finally:
                if connected_at is not None:
                    connected_for = monotonic() - connected_at
                if stream is not None:
                    with anyio.CancelScope(shield=True):
                        await self._close_stream(stream)

            if self._closed:
                return
            if connected_for is not None and connected_for >= _HEALTHY_RESET_AFTER:
                self._backoff = _INITIAL_BACKOFF
            delay = random.uniform(self._backoff / 2, self._backoff)
            self._backoff = min(self._backoff * 2, _MAX_BACKOFF)
            close_event = anyio.Event()
            self._close_event = close_event
            if self._closed:
                close_event.set()
            with anyio.move_on_after(delay):
                await close_event.wait()
            self._close_event = None

    async def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        if self._close_event is not None:
            self._close_event.set()
        if self._cancel_scope is not None:
            self._cancel_scope.cancel()
        if self._stream is not None:
            with anyio.CancelScope(shield=True):
                await self._close_stream(self._stream)

    async def __aenter__(self) -> AsyncResumableStream[T]:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.close()
