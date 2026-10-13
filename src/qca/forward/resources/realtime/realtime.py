from __future__ import annotations

import asyncio
import inspect
import logging
import math
import ssl
import threading
import time
from functools import cached_property
from typing import Any, Literal

import httpx
from websockets.asyncio.client import connect as AsyncConnect
from websockets.exceptions import InvalidHandshake, InvalidStatus
from websockets.sync.client import connect as sync_connect

from qca.common._base_client import AsyncAPIClient, SyncAPIClient
from qca.common._exceptions import APIConnectionError, APITimeoutError, status_error
from qca.common._resource import AsyncAPIResource, SyncAPIResource

from ._protocol import websocket_url
from .connection import AsyncRealtimeConnection, RealtimeConnection
from .conversations import AsyncConversations, Conversations

# Handshake debug logging may include Authorization. Keep the SDK transport silent.
_TRANSPORT_LOGGER = logging.getLogger("qca.realtime.transport")
_TRANSPORT_LOGGER.disabled = True


class _NoRedirectConnect(AsyncConnect):
    def process_redirect(self, exc: Exception) -> Exception | str:
        return exc


def _options(
    handshake_timeout: float,
    ready_timeout: float,
    send_timeout: float,
    close_timeout: float,
    max_queue: int,
    max_queue_bytes: int,
    max_message_bytes: int,
    ssl_context: ssl.SSLContext | None,
    proxy: str | Literal[True] | None,
) -> dict[str, Any]:
    for name, value in (
        ("handshake_timeout", handshake_timeout),
        ("ready_timeout", ready_timeout),
        ("send_timeout", send_timeout),
        ("close_timeout", close_timeout),
    ):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0 or not math.isfinite(value):
            raise ValueError(f"{name} must be a positive finite number")
    for name, value in (
        ("max_queue", max_queue),
        ("max_queue_bytes", max_queue_bytes),
        ("max_message_bytes", max_message_bytes),
    ):
        if type(value) is not int or value < 1:
            raise ValueError(f"{name} must be a positive integer")
    options: dict[str, Any] = dict(
        open_timeout=handshake_timeout,
        close_timeout=close_timeout,
        max_size=max_message_bytes,
        max_queue=8,
        proxy=proxy,
        user_agent_header=None,
        logger=_TRANSPORT_LOGGER,
    )
    if ssl_context is not None:
        options["ssl"] = ssl_context
    return options


def _headers(
    client: SyncAPIClient | AsyncAPIClient, extra_headers: dict[str, str] | None
) -> tuple[httpx.Headers, bool]:
    explicit = any(key.lower() == "authorization" for key in (*client.default_headers, *(extra_headers or {})))
    headers = client._headers({"headers": extra_headers or {}}, client._token)
    return headers, bool(client.credential and client._token is None and not explicit)


def _token(headers: httpx.Headers, token: Any) -> None:
    if not isinstance(token, str) or not token.strip():
        raise ValueError("Credential returned an empty access token")
    headers["Authorization"] = f"Bearer {token}"


def _sync_token(client: SyncAPIClient, timeout: float) -> Any:
    credential = client.credential
    assert credential is not None
    done = threading.Event()
    result: list[Any] = []
    errors: list[Exception] = []

    def resolve() -> None:
        try:
            result.append(credential.get_token())
        except Exception as exc:
            errors.append(exc)
        finally:
            done.set()

    thread = threading.Thread(target=resolve, name="qca-realtime-credential", daemon=True)
    thread.start()
    if not done.wait(timeout):
        raise TimeoutError("Credential resolution timed out")
    if errors:
        raise errors[0]
    return result[0]


async def _async_token(client: AsyncAPIClient) -> Any:
    assert client.credential is not None
    getter = client.credential.get_token
    token = await getter() if inspect.iscoroutinefunction(getter) else await asyncio.to_thread(getter)
    return await token if inspect.isawaitable(token) else token


def _handshake_error(exc: Exception, url: str) -> Exception:
    request = httpx.Request("GET", url)
    if isinstance(exc, InvalidStatus):
        response = httpx.Response(
            exc.response.status_code,
            headers=list(exc.response.headers.raw_items()),
            content=bytes(exc.response.body),
            request=request,
        )
        return status_error(response)
    if isinstance(exc, (TimeoutError, asyncio.TimeoutError)):
        return APITimeoutError(request=request)
    return APIConnectionError(request=request, message="Realtime WebSocket handshake failed")


class Realtime(SyncAPIResource):
    @cached_property
    def conversations(self) -> Conversations:
        return Conversations(self._client)

    def connect(
        self,
        *,
        conversation_id: str,
        extra_headers: dict[str, str] | None = None,
        handshake_timeout: float = 30,
        ready_timeout: float = 60,
        send_timeout: float = 30,
        close_timeout: float = 10,
        max_queue: int = 256,
        max_queue_bytes: int = 4 * 1024 * 1024,
        max_message_bytes: int = 1024 * 1024,
        ssl_context: ssl.SSLContext | None = None,
        proxy: str | Literal[True] | None = True,
    ) -> RealtimeConnection:
        """Connect to /realtime and return after voice.ready. No redirects, retries, or replay."""
        if self._client.is_closed():
            raise RuntimeError("Client is closed")
        url = websocket_url(self._client.base_url, conversation_id)
        options = _options(
            handshake_timeout,
            ready_timeout,
            send_timeout,
            close_timeout,
            max_queue,
            max_queue_bytes,
            max_message_bytes,
            ssl_context,
            proxy,
        )
        headers, dynamic = _headers(self._client, extra_headers)
        deadline = time.monotonic() + handshake_timeout
        try:
            if dynamic:
                _token(headers, _sync_token(self._client, handshake_timeout))
            options["open_timeout"] = max(0, deadline - time.monotonic())
            socket = sync_connect(url, additional_headers=list(headers.multi_items()), **options)
        except (OSError, TimeoutError, asyncio.TimeoutError, InvalidHandshake) as exc:
            raise _handshake_error(exc, url) from exc
        connection = RealtimeConnection(
            socket,
            conversation_id,
            max_queue=max_queue,
            max_queue_bytes=max_queue_bytes,
            send_timeout=send_timeout,
            close_timeout=close_timeout,
        )
        try:
            connection._wait_ready(ready_timeout)
        except BaseException:
            connection.close()
            raise
        return connection


class AsyncRealtime(AsyncAPIResource):
    @cached_property
    def conversations(self) -> AsyncConversations:
        return AsyncConversations(self._client)

    async def connect(
        self,
        *,
        conversation_id: str,
        extra_headers: dict[str, str] | None = None,
        handshake_timeout: float = 30,
        ready_timeout: float = 60,
        send_timeout: float = 30,
        close_timeout: float = 10,
        max_queue: int = 256,
        max_queue_bytes: int = 4 * 1024 * 1024,
        max_message_bytes: int = 1024 * 1024,
        ssl_context: ssl.SSLContext | None = None,
        proxy: str | Literal[True] | None = True,
    ) -> AsyncRealtimeConnection:
        """Connect to /realtime and return after voice.ready. Cancellation releases transport."""
        if self._client.is_closed():
            raise RuntimeError("Client is closed")
        url = websocket_url(self._client.base_url, conversation_id)
        options = _options(
            handshake_timeout,
            ready_timeout,
            send_timeout,
            close_timeout,
            max_queue,
            max_queue_bytes,
            max_message_bytes,
            ssl_context,
            proxy,
        )
        headers, dynamic = _headers(self._client, extra_headers)
        deadline = time.monotonic() + handshake_timeout
        try:
            if dynamic:
                _token(headers, await asyncio.wait_for(_async_token(self._client), handshake_timeout))
            remaining = max(0, deadline - time.monotonic())
            options["open_timeout"] = remaining
            socket = await asyncio.wait_for(
                _NoRedirectConnect(url, additional_headers=list(headers.multi_items()), **options), remaining
            )
        except (OSError, TimeoutError, asyncio.TimeoutError, InvalidHandshake) as exc:
            raise _handshake_error(exc, url) from exc
        connection = AsyncRealtimeConnection(
            socket,
            conversation_id,
            max_queue=max_queue,
            max_queue_bytes=max_queue_bytes,
            send_timeout=send_timeout,
            close_timeout=close_timeout,
        )
        try:
            await connection._wait_ready(ready_timeout)
        except BaseException:
            await connection.close()
            raise
        return connection
