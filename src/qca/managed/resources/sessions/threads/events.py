from __future__ import annotations

from typing import Any, Dict, List, Literal, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._resumable_streaming import (
    AsyncResumableStream,
    ResumableStream,
    _is_terminal_thread_event,
    _resumable_options,
)
from qca.common._streaming import AsyncStream, Stream
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.managed.types.session_event import SessionEvent
from qca.managed.types.stream_session_thread_events_union import StreamSessionThreadEventsUnion

__all__ = ["Events", "AsyncEvents"]


class Events(SyncAPIResource):
    def list(
        self,
        thread_id: str,
        *,
        session_id: str,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[SessionEvent]:
        """GET /sessions/{session_id}/threads/{thread_id}/events."""
        _path = path_template(
            "/sessions/{session_id}/threads/{thread_id}/events", thread_id=thread_id, session_id=session_id
        )
        options = make_request_options(
            body={},
            query={"before_id": before_id, "after_id": after_id, "limit": limit, "page": page},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=SessionEvent, options=options, page_style="PageCursor")

    def stream(
        self,
        thread_id: str,
        *,
        session_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        event_deltas: Union[List[Literal["agent.message", "agent.thinking"]], None, NotGiven] = NOT_GIVEN,
        last_event_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[StreamSessionThreadEventsUnion]:
        """GET /sessions/{session_id}/threads/{thread_id}/stream."""
        _path = path_template(
            "/sessions/{session_id}/threads/{thread_id}/stream", thread_id=thread_id, session_id=session_id
        )
        options = make_request_options(
            body={},
            query={"event_deltas[]": event_deltas},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas, "Last-Event-ID": last_event_id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=StreamSessionThreadEventsUnion, options=options, stream=True)

    def resumable_stream(
        self,
        thread_id: str,
        *,
        session_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        event_deltas: Union[List[Literal["agent.message", "agent.thinking"]], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        last_event_id: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResumableStream[StreamSessionThreadEventsUnion]:
        """Continuously reconnect GET /sessions/{session_id}/threads/{thread_id}/stream."""
        cursor, headers = _resumable_options(last_event_id, extra_headers)
        deltas = list(event_deltas) if isinstance(event_deltas, list) else event_deltas
        beta_values = list(betas) if isinstance(betas, list) else betas
        query = dict(extra_query or {})
        body = dict(extra_body or {})
        return ResumableStream(
            open_stream=lambda next_cursor: self.stream(
                thread_id,
                session_id=session_id,
                workspace_id=workspace_id,
                event_deltas=deltas,
                betas=beta_values,
                last_event_id=next_cursor,
                extra_headers=headers,
                extra_query=query,
                extra_body=body,
                timeout=timeout,
            ),
            retryable=self._client._retryable,
            last_event_id=cursor,
            is_terminal=_is_terminal_thread_event,
        )


class AsyncEvents(AsyncAPIResource):
    def list(
        self,
        thread_id: str,
        *,
        session_id: str,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SessionEvent]:
        """GET /sessions/{session_id}/threads/{thread_id}/events."""
        _path = path_template(
            "/sessions/{session_id}/threads/{thread_id}/events", thread_id=thread_id, session_id=session_id
        )
        options = make_request_options(
            body={},
            query={"before_id": before_id, "after_id": after_id, "limit": limit, "page": page},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=SessionEvent, options=options, page_style="PageCursor")
        )

    async def stream(
        self,
        thread_id: str,
        *,
        session_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        event_deltas: Union[List[Literal["agent.message", "agent.thinking"]], None, NotGiven] = NOT_GIVEN,
        last_event_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[StreamSessionThreadEventsUnion]:
        """GET /sessions/{session_id}/threads/{thread_id}/stream."""
        _path = path_template(
            "/sessions/{session_id}/threads/{thread_id}/stream", thread_id=thread_id, session_id=session_id
        )
        options = make_request_options(
            body={},
            query={"event_deltas[]": event_deltas},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas, "Last-Event-ID": last_event_id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request(
            "GET", _path, cast_to=StreamSessionThreadEventsUnion, options=options, stream=True
        )

    def resumable_stream(
        self,
        thread_id: str,
        *,
        session_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        event_deltas: Union[List[Literal["agent.message", "agent.thinking"]], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        last_event_id: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncResumableStream[StreamSessionThreadEventsUnion]:
        """Continuously reconnect GET /sessions/{session_id}/threads/{thread_id}/stream."""
        cursor, headers = _resumable_options(last_event_id, extra_headers)
        deltas = list(event_deltas) if isinstance(event_deltas, list) else event_deltas
        beta_values = list(betas) if isinstance(betas, list) else betas
        query = dict(extra_query or {})
        body = dict(extra_body or {})
        return AsyncResumableStream(
            open_stream=lambda next_cursor: self.stream(
                thread_id,
                session_id=session_id,
                workspace_id=workspace_id,
                event_deltas=deltas,
                betas=beta_values,
                last_event_id=next_cursor,
                extra_headers=headers,
                extra_query=query,
                extra_body=body,
                timeout=timeout,
            ),
            retryable=self._client._retryable,
            last_event_id=cursor,
            is_terminal=_is_terminal_thread_event,
        )
