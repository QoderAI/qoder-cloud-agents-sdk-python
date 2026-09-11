from __future__ import annotations

from datetime import datetime
from functools import cached_property
from typing import Any, Dict, List, Literal, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.managed.resources.environments.work import AsyncWork, Work
from qca.managed.types.cloud_config_params import CloudConfigParams
from qca.managed.types.environment import Environment
from qca.managed.types.environment_delete_response import EnvironmentDeleteResponse
from qca.managed.types.self_hosted_config_params import SelfHostedConfigParams

__all__ = ["Environments", "AsyncEnvironments"]


class Environments(SyncAPIResource):
    @cached_property
    def work(self) -> Work:
        return Work(self._client)

    def create(
        self,
        *,
        name: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        config: Union[Union[CloudConfigParams, SelfHostedConfigParams], None, NotGiven] = NOT_GIVEN,
        scope: Union[Literal["organization", "account"], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Environment:
        """POST /environments."""
        _path = path_template("/environments")
        options = make_request_options(
            body={"name": name, "description": description, "config": config, "scope": scope, "metadata": metadata},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Environment, options=options)

    def retrieve(
        self,
        environment_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Environment:
        """GET /environments/{environment_id}."""
        _path = path_template("/environments/{environment_id}", environment_id=environment_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Environment, options=options)

    def update(
        self,
        environment_id: str,
        *,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        config: Union[Union[CloudConfigParams, SelfHostedConfigParams], None, NotGiven] = NOT_GIVEN,
        scope: Union[Literal["organization", "account"], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Environment:
        """POST /environments/{environment_id}."""
        _path = path_template("/environments/{environment_id}", environment_id=environment_id)
        options = make_request_options(
            body={"description": description, "name": name, "config": config, "scope": scope, "metadata": metadata},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Environment, options=options)

    def list(
        self,
        *,
        created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Environment]:
        """GET /environments."""
        _path = path_template("/environments")
        options = make_request_options(
            body={},
            query={
                "created_at[gte]": created_at_gte,
                "created_at[lte]": created_at_lte,
                "page": page,
                "include_archived": include_archived,
                "limit": limit,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Environment, options=options, page_style="PageCursor")

    def delete(
        self,
        environment_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentDeleteResponse:
        """DELETE /environments/{environment_id}."""
        _path = path_template("/environments/{environment_id}", environment_id=environment_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("DELETE", _path, cast_to=EnvironmentDeleteResponse, options=options)

    def archive(
        self,
        environment_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Environment:
        """POST /environments/{environment_id}/archive."""
        _path = path_template("/environments/{environment_id}/archive", environment_id=environment_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Environment, options=options)


class AsyncEnvironments(AsyncAPIResource):
    @cached_property
    def work(self) -> AsyncWork:
        return AsyncWork(self._client)

    async def create(
        self,
        *,
        name: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        config: Union[Union[CloudConfigParams, SelfHostedConfigParams], None, NotGiven] = NOT_GIVEN,
        scope: Union[Literal["organization", "account"], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Environment:
        """POST /environments."""
        _path = path_template("/environments")
        options = make_request_options(
            body={"name": name, "description": description, "config": config, "scope": scope, "metadata": metadata},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Environment, options=options)

    async def retrieve(
        self,
        environment_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Environment:
        """GET /environments/{environment_id}."""
        _path = path_template("/environments/{environment_id}", environment_id=environment_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=Environment, options=options)

    async def update(
        self,
        environment_id: str,
        *,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        config: Union[Union[CloudConfigParams, SelfHostedConfigParams], None, NotGiven] = NOT_GIVEN,
        scope: Union[Literal["organization", "account"], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Environment:
        """POST /environments/{environment_id}."""
        _path = path_template("/environments/{environment_id}", environment_id=environment_id)
        options = make_request_options(
            body={"description": description, "name": name, "config": config, "scope": scope, "metadata": metadata},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Environment, options=options)

    def list(
        self,
        *,
        created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Environment]:
        """GET /environments."""
        _path = path_template("/environments")
        options = make_request_options(
            body={},
            query={
                "created_at[gte]": created_at_gte,
                "created_at[lte]": created_at_lte,
                "page": page,
                "include_archived": include_archived,
                "limit": limit,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=Environment, options=options, page_style="PageCursor")
        )

    async def delete(
        self,
        environment_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentDeleteResponse:
        """DELETE /environments/{environment_id}."""
        _path = path_template("/environments/{environment_id}", environment_id=environment_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("DELETE", _path, cast_to=EnvironmentDeleteResponse, options=options)

    async def archive(
        self,
        environment_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Environment:
        """POST /environments/{environment_id}/archive."""
        _path = path_template("/environments/{environment_id}/archive", environment_id=environment_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Environment, options=options)
