from __future__ import annotations

from functools import cached_property
from typing import Any, Dict, List, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.resources.identities.configs import AsyncConfigs, Configs
from qca.forward.resources.identities.memory_stores import AsyncMemoryStores, MemoryStores
from qca.forward.types.deleted_identity import DeletedIdentity
from qca.forward.types.identity import Identity
from qca.forward.types.identity_clear_response import IdentityClearResponse
from qca.forward.types.identity_list_templates_response import IdentityListTemplatesResponse
from qca.forward.types.identity_stats import IdentityStats

__all__ = ["Identities", "AsyncIdentities"]


class Identities(SyncAPIResource):
    @cached_property
    def configs(self) -> Configs:
        return Configs(self._client)

    @cached_property
    def memory_stores(self) -> MemoryStores:
        return MemoryStores(self._client)

    def list(
        self,
        *,
        external_id: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_i_ds: Union[List[str], None, NotGiven] = NOT_GIVEN,
        search: Union[str, None, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Identity]:
        """GET /identities."""
        _path = path_template("/identities")
        options = make_request_options(
            body={},
            query={
                "external_id": external_id,
                "identity_ids": identity_i_ds,
                "search": search,
                "enabled": enabled,
                "limit": limit,
                "after_id": after_id,
                "before_id": before_id,
            },
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Identity, options=options, page_style="Page")

    def create(
        self,
        *,
        external_id: str,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Identity:
        """POST /identities."""
        _path = path_template("/identities")
        options = make_request_options(
            body={"external_id": external_id, "name": name, "enabled": enabled, "metadata": metadata},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Identity, options=options)

    def ensure_admin(
        self,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Identity:
        """POST /identities/admin/ensure."""
        _path = path_template("/identities/admin/ensure")
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Identity, options=options)

    def stats(
        self,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityStats:
        """GET /identities/stats."""
        _path = path_template("/identities/stats")
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=IdentityStats, options=options)

    def retrieve(
        self,
        identity_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Identity:
        """GET /identities/{identity_id}."""
        _path = path_template("/identities/{identity_id}", identity_id=identity_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Identity, options=options)

    def update(
        self,
        identity_id: str,
        *,
        external_id: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Identity:
        """POST /identities/{identity_id}."""
        _path = path_template("/identities/{identity_id}", identity_id=identity_id)
        options = make_request_options(
            body={"external_id": external_id, "name": name, "enabled": enabled, "metadata": metadata},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Identity, options=options)

    def delete(
        self,
        identity_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedIdentity:
        """DELETE /identities/{identity_id}."""
        _path = path_template("/identities/{identity_id}", identity_id=identity_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("DELETE", _path, cast_to=DeletedIdentity, options=options)

    def list_templates(
        self,
        identity_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityListTemplatesResponse:
        """GET /identities/{identity_id}/agents."""
        _path = path_template("/identities/{identity_id}/agents", identity_id=identity_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=IdentityListTemplatesResponse, options=options)

    def clear(
        self,
        identity_id: str,
        *,
        reason: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityClearResponse:
        """POST /identities/{identity_id}/clear."""
        _path = path_template("/identities/{identity_id}/clear", identity_id=identity_id)
        options = make_request_options(
            body={"reason": reason},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=IdentityClearResponse, options=options)

    def disable(
        self,
        identity_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Identity:
        """POST /identities/{identity_id}/disable."""
        _path = path_template("/identities/{identity_id}/disable", identity_id=identity_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Identity, options=options)

    def enable(
        self,
        identity_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Identity:
        """POST /identities/{identity_id}/enable."""
        _path = path_template("/identities/{identity_id}/enable", identity_id=identity_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Identity, options=options)


class AsyncIdentities(AsyncAPIResource):
    @cached_property
    def configs(self) -> AsyncConfigs:
        return AsyncConfigs(self._client)

    @cached_property
    def memory_stores(self) -> AsyncMemoryStores:
        return AsyncMemoryStores(self._client)

    def list(
        self,
        *,
        external_id: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_i_ds: Union[List[str], None, NotGiven] = NOT_GIVEN,
        search: Union[str, None, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Identity]:
        """GET /identities."""
        _path = path_template("/identities")
        options = make_request_options(
            body={},
            query={
                "external_id": external_id,
                "identity_ids": identity_i_ds,
                "search": search,
                "enabled": enabled,
                "limit": limit,
                "after_id": after_id,
                "before_id": before_id,
            },
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=Identity, options=options, page_style="Page")
        )

    async def create(
        self,
        *,
        external_id: str,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Identity:
        """POST /identities."""
        _path = path_template("/identities")
        options = make_request_options(
            body={"external_id": external_id, "name": name, "enabled": enabled, "metadata": metadata},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Identity, options=options)

    async def ensure_admin(
        self,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Identity:
        """POST /identities/admin/ensure."""
        _path = path_template("/identities/admin/ensure")
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Identity, options=options)

    async def stats(
        self,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityStats:
        """GET /identities/stats."""
        _path = path_template("/identities/stats")
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=IdentityStats, options=options)

    async def retrieve(
        self,
        identity_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Identity:
        """GET /identities/{identity_id}."""
        _path = path_template("/identities/{identity_id}", identity_id=identity_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=Identity, options=options)

    async def update(
        self,
        identity_id: str,
        *,
        external_id: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Identity:
        """POST /identities/{identity_id}."""
        _path = path_template("/identities/{identity_id}", identity_id=identity_id)
        options = make_request_options(
            body={"external_id": external_id, "name": name, "enabled": enabled, "metadata": metadata},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Identity, options=options)

    async def delete(
        self,
        identity_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedIdentity:
        """DELETE /identities/{identity_id}."""
        _path = path_template("/identities/{identity_id}", identity_id=identity_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("DELETE", _path, cast_to=DeletedIdentity, options=options)

    async def list_templates(
        self,
        identity_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityListTemplatesResponse:
        """GET /identities/{identity_id}/agents."""
        _path = path_template("/identities/{identity_id}/agents", identity_id=identity_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=IdentityListTemplatesResponse, options=options)

    async def clear(
        self,
        identity_id: str,
        *,
        reason: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityClearResponse:
        """POST /identities/{identity_id}/clear."""
        _path = path_template("/identities/{identity_id}/clear", identity_id=identity_id)
        options = make_request_options(
            body={"reason": reason},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=IdentityClearResponse, options=options)

    async def disable(
        self,
        identity_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Identity:
        """POST /identities/{identity_id}/disable."""
        _path = path_template("/identities/{identity_id}/disable", identity_id=identity_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Identity, options=options)

    async def enable(
        self,
        identity_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Identity:
        """POST /identities/{identity_id}/enable."""
        _path = path_template("/identities/{identity_id}/enable", identity_id=identity_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Identity, options=options)
