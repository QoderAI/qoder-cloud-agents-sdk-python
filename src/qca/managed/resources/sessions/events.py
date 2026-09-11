from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._streaming import AsyncStream, Stream
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.managed.types.send_session_events import SendSessionEvents
from qca.managed.types.session_event import SessionEvent
from qca.managed.types.session_stream_event import SessionStreamEvent
from qca.managed.types.system_message_event_params import SystemMessageEventParams
from qca.managed.types.user_custom_tool_result_event_params import UserCustomToolResultEventParams
from qca.managed.types.user_define_outcome_event_params import UserDefineOutcomeEventParams
from qca.managed.types.user_interrupt_event_params import UserInterruptEventParams
from qca.managed.types.user_message_event_params import UserMessageEventParams
from qca.managed.types.user_tool_confirmation_event_params import UserToolConfirmationEventParams
from qca.managed.types.user_tool_result_event_params import UserToolResultEventParams

__all__ = ["Events", "AsyncEvents"]


class Events(SyncAPIResource):
    def list(
        self,
        session_id: str,
        *,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], None, NotGiven] = NOT_GIVEN,
        types: Union[List[str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
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
                "before_id": before_id,
                "after_id": after_id,
                "created_at[gt]": created_at_gt,
                "created_at[gte]": created_at_gte,
                "created_at[lt]": created_at_lt,
                "created_at[lte]": created_at_lte,
                "limit": limit,
                "page": page,
                "order": order,
                "types[]": types,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=SessionEvent, options=options, page_style="PageCursor")

    def send(
        self,
        session_id: str,
        *,
        events: List[
            Union[
                UserMessageEventParams,
                UserInterruptEventParams,
                UserToolConfirmationEventParams,
                UserCustomToolResultEventParams,
                UserDefineOutcomeEventParams,
                UserToolResultEventParams,
                SystemMessageEventParams,
            ]
        ],
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SendSessionEvents:
        """POST /sessions/{session_id}/events."""
        _path = path_template("/sessions/{session_id}/events", session_id=session_id)
        options = make_request_options(
            body={"events": events},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=SendSessionEvents, options=options)

    def stream(
        self,
        session_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        event_deltas: Union[List[Literal["agent.message", "agent.thinking"]], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[SessionStreamEvent]:
        """GET /sessions/{session_id}/events/stream."""
        _path = path_template("/sessions/{session_id}/events/stream", session_id=session_id)
        options = make_request_options(
            body={},
            query={"event_deltas[]": event_deltas},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=SessionStreamEvent, options=options, stream=True)


class AsyncEvents(AsyncAPIResource):
    def list(
        self,
        session_id: str,
        *,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], None, NotGiven] = NOT_GIVEN,
        types: Union[List[str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
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
                "before_id": before_id,
                "after_id": after_id,
                "created_at[gt]": created_at_gt,
                "created_at[gte]": created_at_gte,
                "created_at[lt]": created_at_lt,
                "created_at[lte]": created_at_lte,
                "limit": limit,
                "page": page,
                "order": order,
                "types[]": types,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=SessionEvent, options=options, page_style="PageCursor")
        )

    async def send(
        self,
        session_id: str,
        *,
        events: List[
            Union[
                UserMessageEventParams,
                UserInterruptEventParams,
                UserToolConfirmationEventParams,
                UserCustomToolResultEventParams,
                UserDefineOutcomeEventParams,
                UserToolResultEventParams,
                SystemMessageEventParams,
            ]
        ],
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SendSessionEvents:
        """POST /sessions/{session_id}/events."""
        _path = path_template("/sessions/{session_id}/events", session_id=session_id)
        options = make_request_options(
            body={"events": events},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=SendSessionEvents, options=options)

    async def stream(
        self,
        session_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        event_deltas: Union[List[Literal["agent.message", "agent.thinking"]], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[SessionStreamEvent]:
        """GET /sessions/{session_id}/events/stream."""
        _path = path_template("/sessions/{session_id}/events/stream", session_id=session_id)
        options = make_request_options(
            body={},
            query={"event_deltas[]": event_deltas},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=SessionStreamEvent, options=options, stream=True)
