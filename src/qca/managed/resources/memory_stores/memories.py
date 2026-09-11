from __future__ import annotations

from typing import Any, Dict, List, Literal, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.managed.types.deleted_memory import DeletedMemory
from qca.managed.types.memory import Memory
from qca.managed.types.memory_list_item_union import MemoryListItemUnion
from qca.managed.types.precondition_param import PreconditionParam

__all__ = ["Memories", "AsyncMemories"]


def _normalize_precondition(body: Dict[str, Any]) -> Dict[str, Any]:
    precondition = body.get("precondition", NOT_GIVEN)
    if isinstance(precondition, NotGiven) or precondition is None:
        return body
    if not isinstance(precondition, dict) or precondition.get("type") != "content_sha256":
        raise ValueError("Unsupported memory precondition")
    expected = precondition.get("content_sha256", NOT_GIVEN)
    explicit = body.get("content_sha256", NOT_GIVEN)
    if not isinstance(explicit, NotGiven) and explicit != expected:
        raise ValueError("Conflicting memory content hashes")
    # The public precondition alias is sent as the API's content_sha256 field.
    return {**body, "content_sha256": expected, "precondition": NOT_GIVEN}


class Memories(SyncAPIResource):
    def create(
        self,
        memory_store_id: str,
        *,
        content: str,
        path: str,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Memory:
        """POST /memory_stores/{memory_store_id}/memories."""
        _path = path_template("/memory_stores/{memory_store_id}/memories", memory_store_id=memory_store_id)
        options = make_request_options(
            body={"metadata": metadata, "content": content, "path": path},
            query={"view": view},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
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
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
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
            query={"view": view},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
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
        content_sha256: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        content: Union[str, None, NotGiven] = NOT_GIVEN,
        path: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
        precondition: Union[PreconditionParam, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
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
            body=_normalize_precondition(
                {
                    "content_sha256": content_sha256,
                    "metadata": metadata,
                    "content": content,
                    "path": path,
                    "precondition": precondition,
                }
            ),
            query={"view": view},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Memory, options=options)

    def list(
        self,
        memory_store_id: str,
        *,
        depth: Union[int, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        path_prefix: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[MemoryListItemUnion]:
        """GET /memory_stores/{memory_store_id}/memories."""
        _path = path_template("/memory_stores/{memory_store_id}/memories", memory_store_id=memory_store_id)
        options = make_request_options(
            body={},
            query={"depth": depth, "limit": limit, "page": page, "path_prefix": path_prefix, "view": view},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=MemoryListItemUnion, options=options, page_style="PageCursor")

    def delete(
        self,
        memory_id: str,
        *,
        memory_store_id: str,
        expected_content_sha256: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
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
            query={"expected_content_sha256": expected_content_sha256},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("DELETE", _path, cast_to=DeletedMemory, options=options)


class AsyncMemories(AsyncAPIResource):
    async def create(
        self,
        memory_store_id: str,
        *,
        content: str,
        path: str,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Memory:
        """POST /memory_stores/{memory_store_id}/memories."""
        _path = path_template("/memory_stores/{memory_store_id}/memories", memory_store_id=memory_store_id)
        options = make_request_options(
            body={"metadata": metadata, "content": content, "path": path},
            query={"view": view},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
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
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
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
            query={"view": view},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
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
        content_sha256: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        content: Union[str, None, NotGiven] = NOT_GIVEN,
        path: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
        precondition: Union[PreconditionParam, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
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
            body=_normalize_precondition(
                {
                    "content_sha256": content_sha256,
                    "metadata": metadata,
                    "content": content,
                    "path": path,
                    "precondition": precondition,
                }
            ),
            query={"view": view},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Memory, options=options)

    def list(
        self,
        memory_store_id: str,
        *,
        depth: Union[int, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        path_prefix: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MemoryListItemUnion]:
        """GET /memory_stores/{memory_store_id}/memories."""
        _path = path_template("/memory_stores/{memory_store_id}/memories", memory_store_id=memory_store_id)
        options = make_request_options(
            body={},
            query={"depth": depth, "limit": limit, "page": page, "path_prefix": path_prefix, "view": view},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request(
                "GET", _path, cast_to=MemoryListItemUnion, options=options, page_style="PageCursor"
            )
        )

    async def delete(
        self,
        memory_id: str,
        *,
        memory_store_id: str,
        expected_content_sha256: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
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
            query={"expected_content_sha256": expected_content_sha256},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("DELETE", _path, cast_to=DeletedMemory, options=options)
