from __future__ import annotations

from functools import cached_property
from typing import Any, Dict, List, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.managed.resources.sessions.threads.events import AsyncEvents, Events
from qca.managed.types.session_thread import SessionThread

__all__ = ["Threads", "AsyncThreads"]


class Threads(SyncAPIResource):
    @cached_property
    def events(self) -> Events:
        return Events(self._client)

    def retrieve(
        self,
        thread_id: str,
        *,
        session_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionThread:
        """GET /sessions/{session_id}/threads/{thread_id}."""
        _path = path_template("/sessions/{session_id}/threads/{thread_id}", thread_id=thread_id, session_id=session_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=SessionThread, options=options)

    def list(
        self,
        session_id: str,
        *,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[SessionThread]:
        """GET /sessions/{session_id}/threads."""
        _path = path_template("/sessions/{session_id}/threads", session_id=session_id)
        options = make_request_options(
            body={},
            query={"limit": limit, "page": page},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=SessionThread, options=options, page_style="PageCursor")

    def archive(
        self,
        thread_id: str,
        *,
        session_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionThread:
        """POST /sessions/{session_id}/threads/{thread_id}/archive."""
        _path = path_template(
            "/sessions/{session_id}/threads/{thread_id}/archive", thread_id=thread_id, session_id=session_id
        )
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=SessionThread, options=options)


class AsyncThreads(AsyncAPIResource):
    @cached_property
    def events(self) -> AsyncEvents:
        return AsyncEvents(self._client)

    async def retrieve(
        self,
        thread_id: str,
        *,
        session_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionThread:
        """GET /sessions/{session_id}/threads/{thread_id}."""
        _path = path_template("/sessions/{session_id}/threads/{thread_id}", thread_id=thread_id, session_id=session_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=SessionThread, options=options)

    def list(
        self,
        session_id: str,
        *,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SessionThread]:
        """GET /sessions/{session_id}/threads."""
        _path = path_template("/sessions/{session_id}/threads", session_id=session_id)
        options = make_request_options(
            body={},
            query={"limit": limit, "page": page},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=SessionThread, options=options, page_style="PageCursor")
        )

    async def archive(
        self,
        thread_id: str,
        *,
        session_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionThread:
        """POST /sessions/{session_id}/threads/{thread_id}/archive."""
        _path = path_template(
            "/sessions/{session_id}/threads/{thread_id}/archive", thread_id=thread_id, session_id=session_id
        )
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=SessionThread, options=options)
