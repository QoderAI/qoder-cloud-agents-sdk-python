from __future__ import annotations

from datetime import datetime
from functools import cached_property
from typing import Any, Dict, List, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.resources.sessions.events import AsyncEvents, Events
from qca.forward.resources.sessions.resources import AsyncResources, Resources
from qca.forward.resources.sessions.threads.threads import AsyncThreads, Threads
from qca.forward.types.session import Session
from qca.forward.types.session_create_params_config_param import SessionCreateParamsConfigParam
from qca.forward.types.session_resource_spec_param import SessionResourceSpecParam
from qca.forward.types.session_update_params_config_param import SessionUpdateParamsConfigParam

__all__ = ["Sessions", "AsyncSessions"]


class Sessions(SyncAPIResource):
    @cached_property
    def events(self) -> Events:
        return Events(self._client)

    @cached_property
    def resources(self) -> Resources:
        return Resources(self._client)

    @cached_property
    def threads(self) -> Threads:
        return Threads(self._client)

    def list(
        self,
        *,
        identity_i_ds: Union[List[str], None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        source_type: Union[str, None, NotGiven] = NOT_GIVEN,
        created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        updated_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        updated_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        updated_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        updated_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        order: Union[str, None, NotGiven] = NOT_GIVEN,
        include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Session]:
        """GET /sessions."""
        _path = path_template("/sessions")
        options = make_request_options(
            body={},
            query={
                "identity_ids": identity_i_ds,
                "template_id": template_id,
                "source_type": source_type,
                "created_at[gt]": created_at_gt,
                "created_at[gte]": created_at_gte,
                "created_at[lt]": created_at_lt,
                "created_at[lte]": created_at_lte,
                "updated_at[gt]": updated_at_gt,
                "updated_at[gte]": updated_at_gte,
                "updated_at[lt]": updated_at_lt,
                "updated_at[lte]": updated_at_lte,
                "limit": limit,
                "after_id": after_id,
                "before_id": before_id,
                "order": order,
                "include_archived": include_archived,
            },
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Session, options=options, page_style="Page")

    def create(
        self,
        *,
        identity_id: str,
        template_id: str,
        title: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        config: Union[SessionCreateParamsConfigParam, None, NotGiven] = NOT_GIVEN,
        resources: Union[List[SessionResourceSpecParam], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """POST /sessions."""
        _path = path_template("/sessions")
        options = make_request_options(
            body={
                "identity_id": identity_id,
                "template_id": template_id,
                "title": title,
                "metadata": metadata,
                "config": config,
                "resources": resources,
            },
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Session, options=options)

    def retrieve(
        self,
        session_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """GET /sessions/{session_id}."""
        _path = path_template("/sessions/{session_id}", session_id=session_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Session, options=options)

    def update(
        self,
        session_id: str,
        *,
        title: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        config: Union[SessionUpdateParamsConfigParam, None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """POST /sessions/{session_id}."""
        _path = path_template("/sessions/{session_id}", session_id=session_id)
        options = make_request_options(
            body={"title": title, "metadata": metadata, "config": config},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Session, options=options)

    def archive(
        self,
        session_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """POST /sessions/{session_id}/archive."""
        _path = path_template("/sessions/{session_id}/archive", session_id=session_id)
        options = make_request_options(
            body={},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Session, options=options)

    def cancel(
        self,
        session_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """POST /sessions/{session_id}/cancel."""
        _path = path_template("/sessions/{session_id}/cancel", session_id=session_id)
        options = make_request_options(
            body={},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Session, options=options)


class AsyncSessions(AsyncAPIResource):
    @cached_property
    def events(self) -> AsyncEvents:
        return AsyncEvents(self._client)

    @cached_property
    def resources(self) -> AsyncResources:
        return AsyncResources(self._client)

    @cached_property
    def threads(self) -> AsyncThreads:
        return AsyncThreads(self._client)

    def list(
        self,
        *,
        identity_i_ds: Union[List[str], None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        source_type: Union[str, None, NotGiven] = NOT_GIVEN,
        created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        updated_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        updated_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        updated_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        updated_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        order: Union[str, None, NotGiven] = NOT_GIVEN,
        include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Session]:
        """GET /sessions."""
        _path = path_template("/sessions")
        options = make_request_options(
            body={},
            query={
                "identity_ids": identity_i_ds,
                "template_id": template_id,
                "source_type": source_type,
                "created_at[gt]": created_at_gt,
                "created_at[gte]": created_at_gte,
                "created_at[lt]": created_at_lt,
                "created_at[lte]": created_at_lte,
                "updated_at[gt]": updated_at_gt,
                "updated_at[gte]": updated_at_gte,
                "updated_at[lt]": updated_at_lt,
                "updated_at[lte]": updated_at_lte,
                "limit": limit,
                "after_id": after_id,
                "before_id": before_id,
                "order": order,
                "include_archived": include_archived,
            },
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=Session, options=options, page_style="Page")
        )

    async def create(
        self,
        *,
        identity_id: str,
        template_id: str,
        title: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        config: Union[SessionCreateParamsConfigParam, None, NotGiven] = NOT_GIVEN,
        resources: Union[List[SessionResourceSpecParam], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """POST /sessions."""
        _path = path_template("/sessions")
        options = make_request_options(
            body={
                "identity_id": identity_id,
                "template_id": template_id,
                "title": title,
                "metadata": metadata,
                "config": config,
                "resources": resources,
            },
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Session, options=options)

    async def retrieve(
        self,
        session_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """GET /sessions/{session_id}."""
        _path = path_template("/sessions/{session_id}", session_id=session_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=Session, options=options)

    async def update(
        self,
        session_id: str,
        *,
        title: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        config: Union[SessionUpdateParamsConfigParam, None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """POST /sessions/{session_id}."""
        _path = path_template("/sessions/{session_id}", session_id=session_id)
        options = make_request_options(
            body={"title": title, "metadata": metadata, "config": config},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Session, options=options)

    async def archive(
        self,
        session_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """POST /sessions/{session_id}/archive."""
        _path = path_template("/sessions/{session_id}/archive", session_id=session_id)
        options = make_request_options(
            body={},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Session, options=options)

    async def cancel(
        self,
        session_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """POST /sessions/{session_id}/cancel."""
        _path = path_template("/sessions/{session_id}/cancel", session_id=session_id)
        options = make_request_options(
            body={},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Session, options=options)
