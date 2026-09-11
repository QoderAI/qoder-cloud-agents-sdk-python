from __future__ import annotations

from typing import Any, Dict, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.types.effective_config import EffectiveConfig
from qca.forward.types.identity_config import IdentityConfig
from qca.forward.types.identity_config_spec_param import IdentityConfigSpecParam

__all__ = ["Configs", "AsyncConfigs"]


class Configs(SyncAPIResource):
    def list(
        self,
        identity_id: str,
        *,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        status: Union[str, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[IdentityConfig]:
        """GET /identities/{identity_id}/templates."""
        _path = path_template("/identities/{identity_id}/templates", identity_id=identity_id)
        options = make_request_options(
            body={},
            query={
                "template_id": template_id,
                "status": status,
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
        return self._client.request("GET", _path, cast_to=IdentityConfig, options=options, page_style="Page")

    def retrieve(
        self,
        template_id: str,
        *,
        identity_id: str,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityConfig:
        """GET /identities/{identity_id}/templates/{template_id}/config."""
        _path = path_template(
            "/identities/{identity_id}/templates/{template_id}/config", template_id=template_id, identity_id=identity_id
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
        return self._client.request("GET", _path, cast_to=IdentityConfig, options=options)

    def upsert(
        self,
        template_id: str,
        *,
        identity_id: str,
        identity_config: IdentityConfigSpecParam,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityConfig:
        """POST /identities/{identity_id}/templates/{template_id}/config."""
        _path = path_template(
            "/identities/{identity_id}/templates/{template_id}/config", template_id=template_id, identity_id=identity_id
        )
        options = make_request_options(
            body={"name": name, "identity_config": identity_config, "metadata": metadata},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=IdentityConfig, options=options)

    def retrieve_effective(
        self,
        template_id: str,
        *,
        identity_id: str,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EffectiveConfig:
        """GET /identities/{identity_id}/templates/{template_id}/effective."""
        _path = path_template(
            "/identities/{identity_id}/templates/{template_id}/effective",
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
        return self._client.request("GET", _path, cast_to=EffectiveConfig, options=options)


class AsyncConfigs(AsyncAPIResource):
    def list(
        self,
        identity_id: str,
        *,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        status: Union[str, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[IdentityConfig]:
        """GET /identities/{identity_id}/templates."""
        _path = path_template("/identities/{identity_id}/templates", identity_id=identity_id)
        options = make_request_options(
            body={},
            query={
                "template_id": template_id,
                "status": status,
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
            lambda: self._client.request("GET", _path, cast_to=IdentityConfig, options=options, page_style="Page")
        )

    async def retrieve(
        self,
        template_id: str,
        *,
        identity_id: str,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityConfig:
        """GET /identities/{identity_id}/templates/{template_id}/config."""
        _path = path_template(
            "/identities/{identity_id}/templates/{template_id}/config", template_id=template_id, identity_id=identity_id
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
        return await self._client.request("GET", _path, cast_to=IdentityConfig, options=options)

    async def upsert(
        self,
        template_id: str,
        *,
        identity_id: str,
        identity_config: IdentityConfigSpecParam,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityConfig:
        """POST /identities/{identity_id}/templates/{template_id}/config."""
        _path = path_template(
            "/identities/{identity_id}/templates/{template_id}/config", template_id=template_id, identity_id=identity_id
        )
        options = make_request_options(
            body={"name": name, "identity_config": identity_config, "metadata": metadata},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=IdentityConfig, options=options)

    async def retrieve_effective(
        self,
        template_id: str,
        *,
        identity_id: str,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EffectiveConfig:
        """GET /identities/{identity_id}/templates/{template_id}/effective."""
        _path = path_template(
            "/identities/{identity_id}/templates/{template_id}/effective",
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
        return await self._client.request("GET", _path, cast_to=EffectiveConfig, options=options)
