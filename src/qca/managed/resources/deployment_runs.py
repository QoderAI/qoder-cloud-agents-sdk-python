from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.managed.types.deployment_run import DeploymentRun

__all__ = ["DeploymentRuns", "AsyncDeploymentRuns"]


class DeploymentRuns(SyncAPIResource):
    def retrieve(
        self,
        deployment_run_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentRun:
        """GET /deployment_runs/{deployment_run_id}."""
        _path = path_template("/deployment_runs/{deployment_run_id}", deployment_run_id=deployment_run_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=DeploymentRun, options=options)

    def list(
        self,
        *,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        deployment_id: Union[str, None, NotGiven] = NOT_GIVEN,
        has_error: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        trigger_type: Union[Literal["schedule", "manual"], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[DeploymentRun]:
        """GET /deployment_runs."""
        _path = path_template("/deployment_runs")
        options = make_request_options(
            body={},
            query={
                "before_id": before_id,
                "after_id": after_id,
                "created_at[gt]": created_at_gt,
                "created_at[gte]": created_at_gte,
                "created_at[lt]": created_at_lt,
                "created_at[lte]": created_at_lte,
                "deployment_id": deployment_id,
                "has_error": has_error,
                "limit": limit,
                "page": page,
                "trigger_type": trigger_type,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=DeploymentRun, options=options, page_style="PageCursor")


class AsyncDeploymentRuns(AsyncAPIResource):
    async def retrieve(
        self,
        deployment_run_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentRun:
        """GET /deployment_runs/{deployment_run_id}."""
        _path = path_template("/deployment_runs/{deployment_run_id}", deployment_run_id=deployment_run_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=DeploymentRun, options=options)

    def list(
        self,
        *,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        deployment_id: Union[str, None, NotGiven] = NOT_GIVEN,
        has_error: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        trigger_type: Union[Literal["schedule", "manual"], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DeploymentRun]:
        """GET /deployment_runs."""
        _path = path_template("/deployment_runs")
        options = make_request_options(
            body={},
            query={
                "before_id": before_id,
                "after_id": after_id,
                "created_at[gt]": created_at_gt,
                "created_at[gte]": created_at_gte,
                "created_at[lt]": created_at_lt,
                "created_at[lte]": created_at_lte,
                "deployment_id": deployment_id,
                "has_error": has_error,
                "limit": limit,
                "page": page,
                "trigger_type": trigger_type,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=DeploymentRun, options=options, page_style="PageCursor")
        )
