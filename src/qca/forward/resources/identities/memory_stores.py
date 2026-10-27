from __future__ import annotations

from typing import Any, Dict, Literal, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.types.deleted_memory_store_mount import DeletedMemoryStoreMount
from qca.forward.types.memory_store_mount import MemoryStoreMount

__all__ = ["MemoryStores", "AsyncMemoryStores"]


class MemoryStores(SyncAPIResource):
    def list(
        self,
        template_id: str,
        *,
        identity_id: str,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        after_id: Union[str, NotGiven] = NOT_GIVEN,
        before_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[MemoryStoreMount]:
        """GET /identities/{identity_id}/templates/{template_id}/memory_stores."""
        _path = path_template(
            "/identities/{identity_id}/templates/{template_id}/memory_stores",
            template_id=template_id,
            identity_id=identity_id,
        )
        options = make_request_options(
            body={},
            query={"limit": limit, "after_id": after_id, "before_id": before_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=MemoryStoreMount, options=options, page_style="Page")

    def mount(
        self,
        template_id: str,
        *,
        identity_id: str,
        memory_store_id: str,
        access: Union[Literal["read_only", "read_write"], NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryStoreMount:
        """POST /identities/{identity_id}/templates/{template_id}/memory_stores."""
        _path = path_template(
            "/identities/{identity_id}/templates/{template_id}/memory_stores",
            template_id=template_id,
            identity_id=identity_id,
        )
        options = make_request_options(
            body={"memory_store_id": memory_store_id, "access": access},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=MemoryStoreMount, options=options)

    def detach(
        self,
        memory_store_id: str,
        *,
        template_id: str,
        identity_id: str,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedMemoryStoreMount:
        """DELETE /identities/{identity_id}/templates/{template_id}/memory_stores/{memory_store_id}."""
        _path = path_template(
            "/identities/{identity_id}/templates/{template_id}/memory_stores/{memory_store_id}",
            memory_store_id=memory_store_id,
            template_id=template_id,
            identity_id=identity_id,
        )
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("DELETE", _path, cast_to=DeletedMemoryStoreMount, options=options)


class AsyncMemoryStores(AsyncAPIResource):
    def list(
        self,
        template_id: str,
        *,
        identity_id: str,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        after_id: Union[str, NotGiven] = NOT_GIVEN,
        before_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MemoryStoreMount]:
        """GET /identities/{identity_id}/templates/{template_id}/memory_stores."""
        _path = path_template(
            "/identities/{identity_id}/templates/{template_id}/memory_stores",
            template_id=template_id,
            identity_id=identity_id,
        )
        options = make_request_options(
            body={},
            query={"limit": limit, "after_id": after_id, "before_id": before_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=MemoryStoreMount, options=options, page_style="Page")
        )

    async def mount(
        self,
        template_id: str,
        *,
        identity_id: str,
        memory_store_id: str,
        access: Union[Literal["read_only", "read_write"], NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryStoreMount:
        """POST /identities/{identity_id}/templates/{template_id}/memory_stores."""
        _path = path_template(
            "/identities/{identity_id}/templates/{template_id}/memory_stores",
            template_id=template_id,
            identity_id=identity_id,
        )
        options = make_request_options(
            body={"memory_store_id": memory_store_id, "access": access},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=MemoryStoreMount, options=options)

    async def detach(
        self,
        memory_store_id: str,
        *,
        template_id: str,
        identity_id: str,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedMemoryStoreMount:
        """DELETE /identities/{identity_id}/templates/{template_id}/memory_stores/{memory_store_id}."""
        _path = path_template(
            "/identities/{identity_id}/templates/{template_id}/memory_stores/{memory_store_id}",
            memory_store_id=memory_store_id,
            template_id=template_id,
            identity_id=identity_id,
        )
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("DELETE", _path, cast_to=DeletedMemoryStoreMount, options=options)
