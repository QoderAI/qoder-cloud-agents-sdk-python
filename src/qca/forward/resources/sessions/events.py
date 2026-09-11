from __future__ import annotations

from typing import Any, Dict, List, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._streaming import AsyncStream, Stream
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.types.session_event import SessionEvent
from qca.forward.types.session_event_param import SessionEventParam
from qca.forward.types.session_event_send_response import SessionEventSendResponse

__all__ = ["Events", "AsyncEvents"]


class Events(SyncAPIResource):
    def list(
        self,
        session_id: str,
        *,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        order: Union[str, None, NotGiven] = NOT_GIVEN,
        type: Union[str, None, NotGiven] = NOT_GIVEN,
        types: Union[List[str], None, NotGiven] = NOT_GIVEN,
        include_tool_calls: Union[bool, None, NotGiven] = NOT_GIVEN,
        include_thinking: Union[bool, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[SessionEvent]:
        """GET /sessions/{session_id}/events."""
        _path = path_template("/sessions/{session_id}/events", session_id=session_id)
        options = make_request_options(
            body={},
            query={
                "limit": limit,
                "after_id": after_id,
                "before_id": before_id,
                "order": order,
                "type": type,
                "types[]": types,
                "include_tool_calls": include_tool_calls,
                "include_thinking": include_thinking,
            },
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=SessionEvent, options=options, page_style="Page")

    def send(
        self,
        session_id: str,
        *,
        events: List[SessionEventParam],
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionEventSendResponse:
        """POST /sessions/{session_id}/events."""
        _path = path_template("/sessions/{session_id}/events", session_id=session_id)
        options = make_request_options(
            body={"events": events},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=SessionEventSendResponse, options=options)

    def stream(
        self,
        session_id: str,
        *,
        event_deltas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        include_tool_calls: Union[bool, None, NotGiven] = NOT_GIVEN,
        include_thinking: Union[bool, None, NotGiven] = NOT_GIVEN,
        last_event_id: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[SessionEvent]:
        """GET /sessions/{session_id}/events/stream."""
        _path = path_template("/sessions/{session_id}/events/stream", session_id=session_id)
        options = make_request_options(
            body={},
            query={
                "event_deltas[]": event_deltas,
                "include_tool_calls": include_tool_calls,
                "include_thinking": include_thinking,
            },
            headers={"Last-Event-ID": last_event_id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=SessionEvent, options=options, stream=True)


class AsyncEvents(AsyncAPIResource):
    def list(
        self,
        session_id: str,
        *,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        order: Union[str, None, NotGiven] = NOT_GIVEN,
        type: Union[str, None, NotGiven] = NOT_GIVEN,
        types: Union[List[str], None, NotGiven] = NOT_GIVEN,
        include_tool_calls: Union[bool, None, NotGiven] = NOT_GIVEN,
        include_thinking: Union[bool, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SessionEvent]:
        """GET /sessions/{session_id}/events."""
        _path = path_template("/sessions/{session_id}/events", session_id=session_id)
        options = make_request_options(
            body={},
            query={
                "limit": limit,
                "after_id": after_id,
                "before_id": before_id,
                "order": order,
                "type": type,
                "types[]": types,
                "include_tool_calls": include_tool_calls,
                "include_thinking": include_thinking,
            },
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=SessionEvent, options=options, page_style="Page")
        )

    async def send(
        self,
        session_id: str,
        *,
        events: List[SessionEventParam],
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionEventSendResponse:
        """POST /sessions/{session_id}/events."""
        _path = path_template("/sessions/{session_id}/events", session_id=session_id)
        options = make_request_options(
            body={"events": events},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=SessionEventSendResponse, options=options)

    async def stream(
        self,
        session_id: str,
        *,
        event_deltas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        include_tool_calls: Union[bool, None, NotGiven] = NOT_GIVEN,
        include_thinking: Union[bool, None, NotGiven] = NOT_GIVEN,
        last_event_id: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[SessionEvent]:
        """GET /sessions/{session_id}/events/stream."""
        _path = path_template("/sessions/{session_id}/events/stream", session_id=session_id)
        options = make_request_options(
            body={},
            query={
                "event_deltas[]": event_deltas,
                "include_tool_calls": include_tool_calls,
                "include_thinking": include_thinking,
            },
            headers={"Last-Event-ID": last_event_id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=SessionEvent, options=options, stream=True)
