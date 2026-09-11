from __future__ import annotations

from typing import Any, Dict, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.types.deleted_memory import DeletedMemory
from qca.forward.types.memory import Memory

__all__ = ["Memories", "AsyncMemories"]


class Memories(SyncAPIResource):
    def list(
        self,
        memory_store_id: str,
        *,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        path_prefix: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Memory]:
        """GET /memory_stores/{memory_store_id}/memories."""
        _path = path_template("/memory_stores/{memory_store_id}/memories", memory_store_id=memory_store_id)
        options = make_request_options(
            body={},
            query={"limit": limit, "before_id": before_id, "after_id": after_id, "path_prefix": path_prefix},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Memory, options=options, page_style="Page")

    def create(
        self,
        memory_store_id: str,
        *,
        path: str,
        content: str,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Memory:
        """POST /memory_stores/{memory_store_id}/memories."""
        _path = path_template("/memory_stores/{memory_store_id}/memories", memory_store_id=memory_store_id)
        options = make_request_options(
            body={"path": path, "content": content, "metadata": metadata},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Memory, options=options)

    def retrieve(
        self,
        memory_id: str,
        *,
        memory_store_id: str,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Memory:
        """GET /memory_stores/{memory_store_id}/memories/{memory_id}."""
        _path = path_template(
            "/memory_stores/{memory_store_id}/memories/{memory_id}",
            memory_id=memory_id,
            memory_store_id=memory_store_id,
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
        return self._client.request("GET", _path, cast_to=Memory, options=options)

    def update(
        self,
        memory_id: str,
        *,
        memory_store_id: str,
        content: str,
        content_sha256: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Memory:
        """POST /memory_stores/{memory_store_id}/memories/{memory_id}."""
        _path = path_template(
            "/memory_stores/{memory_store_id}/memories/{memory_id}",
            memory_id=memory_id,
            memory_store_id=memory_store_id,
        )
        options = make_request_options(
            body={"content": content, "content_sha256": content_sha256, "metadata": metadata},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Memory, options=options)

    def delete(
        self,
        memory_id: str,
        *,
        memory_store_id: str,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedMemory:
        """DELETE /memory_stores/{memory_store_id}/memories/{memory_id}."""
        _path = path_template(
            "/memory_stores/{memory_store_id}/memories/{memory_id}",
            memory_id=memory_id,
            memory_store_id=memory_store_id,
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
        return self._client.request("DELETE", _path, cast_to=DeletedMemory, options=options)


class AsyncMemories(AsyncAPIResource):
    def list(
        self,
        memory_store_id: str,
        *,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        path_prefix: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Memory]:
        """GET /memory_stores/{memory_store_id}/memories."""
        _path = path_template("/memory_stores/{memory_store_id}/memories", memory_store_id=memory_store_id)
        options = make_request_options(
            body={},
            query={"limit": limit, "before_id": before_id, "after_id": after_id, "path_prefix": path_prefix},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=Memory, options=options, page_style="Page")
        )

    async def create(
        self,
        memory_store_id: str,
        *,
        path: str,
        content: str,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Memory:
        """POST /memory_stores/{memory_store_id}/memories."""
        _path = path_template("/memory_stores/{memory_store_id}/memories", memory_store_id=memory_store_id)
        options = make_request_options(
            body={"path": path, "content": content, "metadata": metadata},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Memory, options=options)

    async def retrieve(
        self,
        memory_id: str,
        *,
        memory_store_id: str,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Memory:
        """GET /memory_stores/{memory_store_id}/memories/{memory_id}."""
        _path = path_template(
            "/memory_stores/{memory_store_id}/memories/{memory_id}",
            memory_id=memory_id,
            memory_store_id=memory_store_id,
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
        return await self._client.request("GET", _path, cast_to=Memory, options=options)

    async def update(
        self,
        memory_id: str,
        *,
        memory_store_id: str,
        content: str,
        content_sha256: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Memory:
        """POST /memory_stores/{memory_store_id}/memories/{memory_id}."""
        _path = path_template(
            "/memory_stores/{memory_store_id}/memories/{memory_id}",
            memory_id=memory_id,
            memory_store_id=memory_store_id,
        )
        options = make_request_options(
            body={"content": content, "content_sha256": content_sha256, "metadata": metadata},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Memory, options=options)

    async def delete(
        self,
        memory_id: str,
        *,
        memory_store_id: str,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedMemory:
        """DELETE /memory_stores/{memory_store_id}/memories/{memory_id}."""
        _path = path_template(
            "/memory_stores/{memory_store_id}/memories/{memory_id}",
            memory_id=memory_id,
            memory_store_id=memory_store_id,
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
        return await self._client.request("DELETE", _path, cast_to=DeletedMemory, options=options)
