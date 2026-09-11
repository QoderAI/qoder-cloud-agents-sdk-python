from __future__ import annotations

from typing import Any, Dict, List, Literal, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
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
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=StreamSessionThreadEventsUnion, options=options, stream=True)


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
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request(
            "GET", _path, cast_to=StreamSessionThreadEventsUnion, options=options, stream=True
        )
