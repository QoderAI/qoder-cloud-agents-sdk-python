from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.managed.types.agent_params import AgentParams
from qca.managed.types.budget_limit_param import BudgetLimitParam
from qca.managed.types.deployment import Deployment
from qca.managed.types.deployment_run import DeploymentRun
from qca.managed.types.file_resource_params import FileResourceParams
from qca.managed.types.git_hub_repository_resource_params import GitHubRepositoryResourceParams
from qca.managed.types.memory_store_resource_param import MemoryStoreResourceParam
from qca.managed.types.schedule_params import ScheduleParams
from qca.managed.types.system_message_event_params import SystemMessageEventParams
from qca.managed.types.user_define_outcome_event_params import UserDefineOutcomeEventParams
from qca.managed.types.user_message_event_params import UserMessageEventParams

__all__ = ["Deployments", "AsyncDeployments"]


class Deployments(SyncAPIResource):
    def create(
        self,
        *,
        agent: Union[str, AgentParams],
        environment_id: str,
        initial_events: List[Union[UserMessageEventParams, UserDefineOutcomeEventParams, SystemMessageEventParams]],
        name: str,
        environment_variables: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        budget: Union[BudgetLimitParam, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        resources: Union[
            List[Union[GitHubRepositoryResourceParams, FileResourceParams, MemoryStoreResourceParam]], None, NotGiven
        ] = NOT_GIVEN,
        schedule: Union[ScheduleParams, None, NotGiven] = NOT_GIVEN,
        vault_ids: Union[List[str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Deployment:
        """POST /deployments."""
        _path = path_template("/deployments")
        options = make_request_options(
            body={
                "environment_variables": environment_variables,
                "agent": agent,
                "environment_id": environment_id,
                "initial_events": initial_events,
                "name": name,
                "description": description,
                "budget": budget,
                "metadata": metadata,
                "resources": resources,
                "schedule": schedule,
                "vault_ids": vault_ids,
            },
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Deployment, options=options)

    def retrieve(
        self,
        deployment_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Deployment:
        """GET /deployments/{deployment_id}."""
        _path = path_template("/deployments/{deployment_id}", deployment_id=deployment_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Deployment, options=options)

    def update(
        self,
        deployment_id: str,
        *,
        environment_variables: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        environment_id: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        resources: Union[
            List[Union[GitHubRepositoryResourceParams, FileResourceParams, MemoryStoreResourceParam]], None, NotGiven
        ] = NOT_GIVEN,
        vault_ids: Union[List[str], None, NotGiven] = NOT_GIVEN,
        agent: Union[Union[str, AgentParams], None, NotGiven] = NOT_GIVEN,
        budget: Union[BudgetLimitParam, None, NotGiven] = NOT_GIVEN,
        initial_events: Union[
            List[Union[UserMessageEventParams, UserDefineOutcomeEventParams, SystemMessageEventParams]], None, NotGiven
        ] = NOT_GIVEN,
        schedule: Union[ScheduleParams, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Deployment:
        """POST /deployments/{deployment_id}."""
        _path = path_template("/deployments/{deployment_id}", deployment_id=deployment_id)
        options = make_request_options(
            body={
                "environment_variables": environment_variables,
                "description": description,
                "environment_id": environment_id,
                "name": name,
                "metadata": metadata,
                "resources": resources,
                "vault_ids": vault_ids,
                "agent": agent,
                "budget": budget,
                "initial_events": initial_events,
                "schedule": schedule,
            },
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Deployment, options=options)

    def list(
        self,
        *,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        agent_id: Union[str, None, NotGiven] = NOT_GIVEN,
        created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        status: Union[Literal["active", "paused"], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Deployment]:
        """GET /deployments."""
        _path = path_template("/deployments")
        options = make_request_options(
            body={},
            query={
                "before_id": before_id,
                "after_id": after_id,
                "agent_id": agent_id,
                "created_at[gte]": created_at_gte,
                "created_at[lte]": created_at_lte,
                "include_archived": include_archived,
                "limit": limit,
                "page": page,
                "status": status,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Deployment, options=options, page_style="PageCursor")

    def archive(
        self,
        deployment_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Deployment:
        """POST /deployments/{deployment_id}/archive."""
        _path = path_template("/deployments/{deployment_id}/archive", deployment_id=deployment_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Deployment, options=options)

    def pause(
        self,
        deployment_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Deployment:
        """POST /deployments/{deployment_id}/pause."""
        _path = path_template("/deployments/{deployment_id}/pause", deployment_id=deployment_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Deployment, options=options)

    def run(
        self,
        deployment_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentRun:
        """POST /deployments/{deployment_id}/run."""
        _path = path_template("/deployments/{deployment_id}/run", deployment_id=deployment_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=DeploymentRun, options=options)

    def unpause(
        self,
        deployment_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Deployment:
        """POST /deployments/{deployment_id}/unpause."""
        _path = path_template("/deployments/{deployment_id}/unpause", deployment_id=deployment_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Deployment, options=options)


class AsyncDeployments(AsyncAPIResource):
    async def create(
        self,
        *,
        agent: Union[str, AgentParams],
        environment_id: str,
        initial_events: List[Union[UserMessageEventParams, UserDefineOutcomeEventParams, SystemMessageEventParams]],
        name: str,
        environment_variables: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        budget: Union[BudgetLimitParam, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        resources: Union[
            List[Union[GitHubRepositoryResourceParams, FileResourceParams, MemoryStoreResourceParam]], None, NotGiven
        ] = NOT_GIVEN,
        schedule: Union[ScheduleParams, None, NotGiven] = NOT_GIVEN,
        vault_ids: Union[List[str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Deployment:
        """POST /deployments."""
        _path = path_template("/deployments")
        options = make_request_options(
            body={
                "environment_variables": environment_variables,
                "agent": agent,
                "environment_id": environment_id,
                "initial_events": initial_events,
                "name": name,
                "description": description,
                "budget": budget,
                "metadata": metadata,
                "resources": resources,
                "schedule": schedule,
                "vault_ids": vault_ids,
            },
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Deployment, options=options)

    async def retrieve(
        self,
        deployment_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Deployment:
        """GET /deployments/{deployment_id}."""
        _path = path_template("/deployments/{deployment_id}", deployment_id=deployment_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=Deployment, options=options)

    async def update(
        self,
        deployment_id: str,
        *,
        environment_variables: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        environment_id: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        resources: Union[
            List[Union[GitHubRepositoryResourceParams, FileResourceParams, MemoryStoreResourceParam]], None, NotGiven
        ] = NOT_GIVEN,
        vault_ids: Union[List[str], None, NotGiven] = NOT_GIVEN,
        agent: Union[Union[str, AgentParams], None, NotGiven] = NOT_GIVEN,
        budget: Union[BudgetLimitParam, None, NotGiven] = NOT_GIVEN,
        initial_events: Union[
            List[Union[UserMessageEventParams, UserDefineOutcomeEventParams, SystemMessageEventParams]], None, NotGiven
        ] = NOT_GIVEN,
        schedule: Union[ScheduleParams, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Deployment:
        """POST /deployments/{deployment_id}."""
        _path = path_template("/deployments/{deployment_id}", deployment_id=deployment_id)
        options = make_request_options(
            body={
                "environment_variables": environment_variables,
                "description": description,
                "environment_id": environment_id,
                "name": name,
                "metadata": metadata,
                "resources": resources,
                "vault_ids": vault_ids,
                "agent": agent,
                "budget": budget,
                "initial_events": initial_events,
                "schedule": schedule,
            },
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Deployment, options=options)

    def list(
        self,
        *,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        agent_id: Union[str, None, NotGiven] = NOT_GIVEN,
        created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        status: Union[Literal["active", "paused"], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Deployment]:
        """GET /deployments."""
        _path = path_template("/deployments")
        options = make_request_options(
            body={},
            query={
                "before_id": before_id,
                "after_id": after_id,
                "agent_id": agent_id,
                "created_at[gte]": created_at_gte,
                "created_at[lte]": created_at_lte,
                "include_archived": include_archived,
                "limit": limit,
                "page": page,
                "status": status,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=Deployment, options=options, page_style="PageCursor")
        )

    async def archive(
        self,
        deployment_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Deployment:
        """POST /deployments/{deployment_id}/archive."""
        _path = path_template("/deployments/{deployment_id}/archive", deployment_id=deployment_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Deployment, options=options)

    async def pause(
        self,
        deployment_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Deployment:
        """POST /deployments/{deployment_id}/pause."""
        _path = path_template("/deployments/{deployment_id}/pause", deployment_id=deployment_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Deployment, options=options)

    async def run(
        self,
        deployment_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentRun:
        """POST /deployments/{deployment_id}/run."""
        _path = path_template("/deployments/{deployment_id}/run", deployment_id=deployment_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=DeploymentRun, options=options)

    async def unpause(
        self,
        deployment_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Deployment:
        """POST /deployments/{deployment_id}/unpause."""
        _path = path_template("/deployments/{deployment_id}/unpause", deployment_id=deployment_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Deployment, options=options)
