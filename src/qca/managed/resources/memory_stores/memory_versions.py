from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.managed.types.memory_version import MemoryVersion

__all__ = ["MemoryVersions", "AsyncMemoryVersions"]


class MemoryVersions(SyncAPIResource):
    def retrieve(
        self,
        memory_version_id: str,
        *,
        memory_store_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryVersion:
        """GET /memory_stores/{memory_store_id}/memory_versions/{memory_version_id}."""
        _path = path_template(
            "/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}",
            memory_version_id=memory_version_id,
            memory_store_id=memory_store_id,
        )
        options = make_request_options(
            body={},
            query={"view": view},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=MemoryVersion, options=options)

    def list(
        self,
        memory_store_id: str,
        *,
        api_key_id: Union[str, None, NotGiven] = NOT_GIVEN,
        created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        memory_id: Union[str, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        service_account_id: Union[str, None, NotGiven] = NOT_GIVEN,
        session_id: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        operation: Union[Literal["created", "modified", "deleted"], None, NotGiven] = NOT_GIVEN,
        view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[MemoryVersion]:
        """GET /memory_stores/{memory_store_id}/memory_versions."""
        _path = path_template("/memory_stores/{memory_store_id}/memory_versions", memory_store_id=memory_store_id)
        options = make_request_options(
            body={},
            query={
                "api_key_id": api_key_id,
                "created_at[gte]": created_at_gte,
                "created_at[lte]": created_at_lte,
                "limit": limit,
                "memory_id": memory_id,
                "page": page,
                "service_account_id": service_account_id,
                "session_id": session_id,
                "operation": operation,
                "view": view,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=MemoryVersion, options=options, page_style="PageCursor")

    def redact(
        self,
        memory_version_id: str,
        *,
        memory_store_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryVersion:
        """POST /memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact."""
        _path = path_template(
            "/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact",
            memory_version_id=memory_version_id,
            memory_store_id=memory_store_id,
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
        return self._client.request("POST", _path, cast_to=MemoryVersion, options=options)


class AsyncMemoryVersions(AsyncAPIResource):
    async def retrieve(
        self,
        memory_version_id: str,
        *,
        memory_store_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryVersion:
        """GET /memory_stores/{memory_store_id}/memory_versions/{memory_version_id}."""
        _path = path_template(
            "/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}",
            memory_version_id=memory_version_id,
            memory_store_id=memory_store_id,
        )
        options = make_request_options(
            body={},
            query={"view": view},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=MemoryVersion, options=options)

    def list(
        self,
        memory_store_id: str,
        *,
        api_key_id: Union[str, None, NotGiven] = NOT_GIVEN,
        created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        memory_id: Union[str, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        service_account_id: Union[str, None, NotGiven] = NOT_GIVEN,
        session_id: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        operation: Union[Literal["created", "modified", "deleted"], None, NotGiven] = NOT_GIVEN,
        view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MemoryVersion]:
        """GET /memory_stores/{memory_store_id}/memory_versions."""
        _path = path_template("/memory_stores/{memory_store_id}/memory_versions", memory_store_id=memory_store_id)
        options = make_request_options(
            body={},
            query={
                "api_key_id": api_key_id,
                "created_at[gte]": created_at_gte,
                "created_at[lte]": created_at_lte,
                "limit": limit,
                "memory_id": memory_id,
                "page": page,
                "service_account_id": service_account_id,
                "session_id": session_id,
                "operation": operation,
                "view": view,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=MemoryVersion, options=options, page_style="PageCursor")
        )

    async def redact(
        self,
        memory_version_id: str,
        *,
        memory_store_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryVersion:
        """POST /memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact."""
        _path = path_template(
            "/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact",
            memory_version_id=memory_version_id,
            memory_store_id=memory_store_id,
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
        return await self._client.request("POST", _path, cast_to=MemoryVersion, options=options)
