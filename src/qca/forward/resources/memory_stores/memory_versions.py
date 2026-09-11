from __future__ import annotations

from typing import Any, Dict, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.types.memory_version import MemoryVersion

__all__ = ["MemoryVersions", "AsyncMemoryVersions"]


class MemoryVersions(SyncAPIResource):
    def list(
        self,
        memory_store_id: str,
        *,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        memory_id: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[MemoryVersion]:
        """GET /memory_stores/{memory_store_id}/memory_versions."""
        _path = path_template("/memory_stores/{memory_store_id}/memory_versions", memory_store_id=memory_store_id)
        options = make_request_options(
            body={},
            query={"limit": limit, "before_id": before_id, "after_id": after_id, "memory_id": memory_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=MemoryVersion, options=options, page_style="Page")

    def retrieve(
        self,
        memory_version_id: str,
        *,
        memory_store_id: str,
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
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=MemoryVersion, options=options)

    def redact(
        self,
        memory_version_id: str,
        *,
        memory_store_id: str,
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
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=MemoryVersion, options=options)


class AsyncMemoryVersions(AsyncAPIResource):
    def list(
        self,
        memory_store_id: str,
        *,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        memory_id: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MemoryVersion]:
        """GET /memory_stores/{memory_store_id}/memory_versions."""
        _path = path_template("/memory_stores/{memory_store_id}/memory_versions", memory_store_id=memory_store_id)
        options = make_request_options(
            body={},
            query={"limit": limit, "before_id": before_id, "after_id": after_id, "memory_id": memory_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=MemoryVersion, options=options, page_style="Page")
        )

    async def retrieve(
        self,
        memory_version_id: str,
        *,
        memory_store_id: str,
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
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=MemoryVersion, options=options)

    async def redact(
        self,
        memory_version_id: str,
        *,
        memory_store_id: str,
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
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=MemoryVersion, options=options)
