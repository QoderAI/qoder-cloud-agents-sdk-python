from __future__ import annotations

from typing import Any, Callable

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._response import APIResponse, AsyncAPIResponse
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.forward.types.realtime import (
    AsyncRealtimeHistoryPage,
    RealtimeConfigParam,
    RealtimeConversation,
    RealtimeHistoryPage,
)


def _create_options(
    identity_id: str,
    template_id: str,
    idempotency_key: str,
    title: Any,
    metadata: Any,
    config: Any,
    extra_headers: Any,
    extra_query: Any,
    extra_body: Any,
    timeout: Any,
) -> dict[str, Any]:
    headers = httpx.Headers(extra_headers or {})
    key = headers.get("Idempotency-Key", idempotency_key)
    if (
        not isinstance(key, str)
        or not 1 <= len(key.encode("utf-8")) <= 256
        or key != key.strip()
        or any(ord(c) < 32 or ord(c) == 127 for c in key)
    ):
        raise ValueError("idempotency_key must be 1–256 UTF-8 bytes without surrounding whitespace or controls")
    headers["Idempotency-Key"] = key
    return make_request_options(
        body={
            "identity_id": identity_id,
            "template_id": template_id,
            "title": title,
            "metadata": metadata,
            "config": config,
        },
        query={},
        headers={},
        extra_headers=dict(headers),
        extra_query=extra_query,
        extra_body=extra_body,
        timeout=timeout,
    )


def _history_options(
    limit: Any, before: Any, types: Any, extra_headers: Any, extra_query: Any, extra_body: Any, timeout: Any
) -> dict[str, Any]:
    if not isinstance(limit, NotGiven) and (
        isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 100
    ):
        raise ValueError("limit must be an integer from 1 to 100")
    if not isinstance(before, NotGiven) and (not isinstance(before, str) or not before):
        raise ValueError("before must be a non-empty cursor")
    if not isinstance(types, NotGiven) and types not in ("message", "work", "message,work"):
        raise ValueError("types must be message, work, or message,work")
    return make_request_options(
        body={},
        query={"limit": limit, "before": before, "types": types},
        headers={},
        extra_headers=extra_headers,
        extra_query=extra_query,
        extra_body=extra_body,
        timeout=timeout,
    )


def _bind_history(result: Any, fetch: Callable[[str], Any]) -> Any:
    if isinstance(result, (APIResponse, AsyncAPIResponse)):
        parse = result._parse
        result._parse = lambda: _bind_history(parse(), fetch)
    else:
        result._fetch_next = fetch
    return result


class Conversations(SyncAPIResource):
    def create(
        self,
        *,
        identity_id: str,
        template_id: str,
        idempotency_key: str,
        title: str | None | NotGiven = NOT_GIVEN,
        metadata: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        config: RealtimeConfigParam | NotGiven = NOT_GIVEN,
        extra_headers: dict[str, str] | None = None,
        extra_query: dict[str, Any] | None = None,
        extra_body: dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RealtimeConversation:
        """POST /realtime/conversations. Requires a stable creation idempotency key."""
        options = _create_options(
            identity_id,
            template_id,
            idempotency_key,
            title,
            metadata,
            config,
            extra_headers,
            extra_query,
            extra_body,
            timeout,
        )
        return self._client.request("POST", "/realtime/conversations", cast_to=RealtimeConversation, options=options)

    def history(
        self,
        conversation_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        types: str | NotGiven = NOT_GIVEN,
        extra_headers: dict[str, str] | None = None,
        extra_query: dict[str, Any] | None = None,
        extra_body: dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RealtimeHistoryPage:
        """GET /realtime/conversations/{conversation_id}/history. Pages move toward older events."""
        options = _history_options(limit, before, types, extra_headers, extra_query, extra_body, timeout)
        result = self._client.request(
            "GET",
            path_template("/realtime/conversations/{conversation_id}/history", conversation_id=conversation_id),
            cast_to=RealtimeHistoryPage,
            options=options,
        )
        pager = Conversations(self._client.with_options())
        return _bind_history(
            result,
            lambda cursor: pager.history(
                conversation_id,
                limit=limit,
                before=cursor,
                types=types,
                extra_headers=extra_headers,
                extra_query={k: v for k, v in (extra_query or {}).items() if k != "before"},
                extra_body=extra_body,
                timeout=timeout,
            ),
        )


class AsyncConversations(AsyncAPIResource):
    async def create(
        self,
        *,
        identity_id: str,
        template_id: str,
        idempotency_key: str,
        title: str | None | NotGiven = NOT_GIVEN,
        metadata: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        config: RealtimeConfigParam | NotGiven = NOT_GIVEN,
        extra_headers: dict[str, str] | None = None,
        extra_query: dict[str, Any] | None = None,
        extra_body: dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RealtimeConversation:
        """POST /realtime/conversations. Requires a stable creation idempotency key."""
        options = _create_options(
            identity_id,
            template_id,
            idempotency_key,
            title,
            metadata,
            config,
            extra_headers,
            extra_query,
            extra_body,
            timeout,
        )
        return await self._client.request(
            "POST", "/realtime/conversations", cast_to=RealtimeConversation, options=options
        )

    async def history(
        self,
        conversation_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        types: str | NotGiven = NOT_GIVEN,
        extra_headers: dict[str, str] | None = None,
        extra_query: dict[str, Any] | None = None,
        extra_body: dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncRealtimeHistoryPage:
        """GET /realtime/conversations/{conversation_id}/history. Await get_next_page() for older events."""
        options = _history_options(limit, before, types, extra_headers, extra_query, extra_body, timeout)
        result = await self._client.request(
            "GET",
            path_template("/realtime/conversations/{conversation_id}/history", conversation_id=conversation_id),
            cast_to=AsyncRealtimeHistoryPage,
            options=options,
        )
        pager = AsyncConversations(self._client.with_options())
        return _bind_history(
            result,
            lambda cursor: pager.history(
                conversation_id,
                limit=limit,
                before=cursor,
                types=types,
                extra_headers=extra_headers,
                extra_query={k: v for k, v in (extra_query or {}).items() if k != "before"},
                extra_body=extra_body,
                timeout=timeout,
            ),
        )
