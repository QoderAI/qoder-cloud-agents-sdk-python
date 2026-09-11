from __future__ import annotations

from datetime import datetime
from functools import cached_property
from typing import Any, Dict, List, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.managed.resources.memory_stores.memories import AsyncMemories, Memories
from qca.managed.resources.memory_stores.memory_versions import AsyncMemoryVersions, MemoryVersions
from qca.managed.types.deleted_memory_store import DeletedMemoryStore
from qca.managed.types.memory_store import MemoryStore

__all__ = ["MemoryStores", "AsyncMemoryStores"]


class MemoryStores(SyncAPIResource):
    @cached_property
    def memories(self) -> Memories:
        return Memories(self._client)

    @cached_property
    def memory_versions(self) -> MemoryVersions:
        return MemoryVersions(self._client)

    def create(
        self,
        *,
        name: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryStore:
        """POST /memory_stores."""
        _path = path_template("/memory_stores")
        options = make_request_options(
            body={"name": name, "description": description, "metadata": metadata},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=MemoryStore, options=options)

    def retrieve(
        self,
        memory_store_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryStore:
        """GET /memory_stores/{memory_store_id}."""
        _path = path_template("/memory_stores/{memory_store_id}", memory_store_id=memory_store_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=MemoryStore, options=options)

    def update(
        self,
        memory_store_id: str,
        *,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryStore:
        """POST /memory_stores/{memory_store_id}."""
        _path = path_template("/memory_stores/{memory_store_id}", memory_store_id=memory_store_id)
        options = make_request_options(
            body={"description": description, "name": name, "metadata": metadata},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=MemoryStore, options=options)

    def list(
        self,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[MemoryStore]:
        """GET /memory_stores."""
        _path = path_template("/memory_stores")
        options = make_request_options(
            body={},
            query={
                "name": name,
                "created_at[gte]": created_at_gte,
                "created_at[lte]": created_at_lte,
                "include_archived": include_archived,
                "limit": limit,
                "page": page,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=MemoryStore, options=options, page_style="PageCursor")

    def delete(
        self,
        memory_store_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedMemoryStore:
        """DELETE /memory_stores/{memory_store_id}."""
        _path = path_template("/memory_stores/{memory_store_id}", memory_store_id=memory_store_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("DELETE", _path, cast_to=DeletedMemoryStore, options=options)

    def archive(
        self,
        memory_store_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryStore:
        """POST /memory_stores/{memory_store_id}/archive."""
        _path = path_template("/memory_stores/{memory_store_id}/archive", memory_store_id=memory_store_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=MemoryStore, options=options)


class AsyncMemoryStores(AsyncAPIResource):
    @cached_property
    def memories(self) -> AsyncMemories:
        return AsyncMemories(self._client)

    @cached_property
    def memory_versions(self) -> AsyncMemoryVersions:
        return AsyncMemoryVersions(self._client)

    async def create(
        self,
        *,
        name: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryStore:
        """POST /memory_stores."""
        _path = path_template("/memory_stores")
        options = make_request_options(
            body={"name": name, "description": description, "metadata": metadata},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=MemoryStore, options=options)

    async def retrieve(
        self,
        memory_store_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryStore:
        """GET /memory_stores/{memory_store_id}."""
        _path = path_template("/memory_stores/{memory_store_id}", memory_store_id=memory_store_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=MemoryStore, options=options)

    async def update(
        self,
        memory_store_id: str,
        *,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryStore:
        """POST /memory_stores/{memory_store_id}."""
        _path = path_template("/memory_stores/{memory_store_id}", memory_store_id=memory_store_id)
        options = make_request_options(
            body={"description": description, "name": name, "metadata": metadata},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=MemoryStore, options=options)

    def list(
        self,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MemoryStore]:
        """GET /memory_stores."""
        _path = path_template("/memory_stores")
        options = make_request_options(
            body={},
            query={
                "name": name,
                "created_at[gte]": created_at_gte,
                "created_at[lte]": created_at_lte,
                "include_archived": include_archived,
                "limit": limit,
                "page": page,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=MemoryStore, options=options, page_style="PageCursor")
        )

    async def delete(
        self,
        memory_store_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedMemoryStore:
        """DELETE /memory_stores/{memory_store_id}."""
        _path = path_template("/memory_stores/{memory_store_id}", memory_store_id=memory_store_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("DELETE", _path, cast_to=DeletedMemoryStore, options=options)

    async def archive(
        self,
        memory_store_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryStore:
        """POST /memory_stores/{memory_store_id}/archive."""
        _path = path_template("/memory_stores/{memory_store_id}/archive", memory_store_id=memory_store_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=MemoryStore, options=options)
