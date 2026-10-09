from __future__ import annotations

from typing import Any, Dict, List, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.managed.types.deployment_run import DeploymentRun

__all__ = ["Runs", "AsyncRuns"]


class Runs(SyncAPIResource):
    def list(
        self,
        deployment_id: str,
        *,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        triggered_after: Union[str, None, NotGiven] = NOT_GIVEN,
        triggered_before: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[DeploymentRun]:
        """GET /deployments/{deployment_id}/runs."""
        _path = path_template("/deployments/{deployment_id}/runs", deployment_id=deployment_id)
        options = make_request_options(
            body={},
            query={
                "limit": limit,
                "page": page,
                "after_id": after_id,
                "before_id": before_id,
                "triggered_after": triggered_after,
                "triggered_before": triggered_before,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=DeploymentRun, options=options, page_style="PageCursor")

    def retrieve(
        self,
        run_id: str,
        *,
        deployment_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentRun:
        """GET /deployments/{deployment_id}/runs/{run_id}."""
        _path = path_template("/deployments/{deployment_id}/runs/{run_id}", deployment_id=deployment_id, run_id=run_id)
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


class AsyncRuns(AsyncAPIResource):
    def list(
        self,
        deployment_id: str,
        *,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        triggered_after: Union[str, None, NotGiven] = NOT_GIVEN,
        triggered_before: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DeploymentRun]:
        """GET /deployments/{deployment_id}/runs."""
        _path = path_template("/deployments/{deployment_id}/runs", deployment_id=deployment_id)
        options = make_request_options(
            body={},
            query={
                "limit": limit,
                "page": page,
                "after_id": after_id,
                "before_id": before_id,
                "triggered_after": triggered_after,
                "triggered_before": triggered_before,
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

    async def retrieve(
        self,
        run_id: str,
        *,
        deployment_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentRun:
        """GET /deployments/{deployment_id}/runs/{run_id}."""
        _path = path_template("/deployments/{deployment_id}/runs/{run_id}", deployment_id=deployment_id, run_id=run_id)
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
