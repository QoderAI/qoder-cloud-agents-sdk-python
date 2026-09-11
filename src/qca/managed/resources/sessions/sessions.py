from __future__ import annotations

from datetime import datetime
from functools import cached_property
from typing import Any, Dict, List, Literal, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.managed.resources.sessions.events import AsyncEvents, Events
from qca.managed.resources.sessions.resources import AsyncResources, Resources
from qca.managed.resources.sessions.threads.threads import AsyncThreads, Threads
from qca.managed.types.agent_params import AgentParams
from qca.managed.types.agent_with_overrides_params import AgentWithOverridesParams
from qca.managed.types.budget_limit_param import BudgetLimitParam
from qca.managed.types.deleted_session import DeletedSession
from qca.managed.types.file_resource_params import FileResourceParams
from qca.managed.types.git_hub_repository_resource_params import GitHubRepositoryResourceParams
from qca.managed.types.memory_store_resource_param import MemoryStoreResourceParam
from qca.managed.types.session import Session
from qca.managed.types.session_agent_update_param import SessionAgentUpdateParam
from qca.managed.types.user_define_outcome_event_params import UserDefineOutcomeEventParams
from qca.managed.types.user_message_event_params import UserMessageEventParams

__all__ = ["Sessions", "AsyncSessions"]


class Sessions(SyncAPIResource):
    @cached_property
    def events(self) -> Events:
        return Events(self._client)

    @cached_property
    def resources(self) -> Resources:
        return Resources(self._client)

    @cached_property
    def threads(self) -> Threads:
        return Threads(self._client)

    def create(
        self,
        *,
        agent: Union[str, AgentParams, AgentWithOverridesParams],
        environment_id: str,
        environment_variables: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        title: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        budget: Union[BudgetLimitParam, None, NotGiven] = NOT_GIVEN,
        initial_events: Union[
            List[Union[UserMessageEventParams, UserDefineOutcomeEventParams]], None, NotGiven
        ] = NOT_GIVEN,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        resources: Union[
            List[Union[GitHubRepositoryResourceParams, FileResourceParams, MemoryStoreResourceParam]], None, NotGiven
        ] = NOT_GIVEN,
        vault_ids: Union[List[str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """POST /sessions."""
        _path = path_template("/sessions")
        options = make_request_options(
            body={
                "environment_variables": environment_variables,
                "agent": agent,
                "environment_id": environment_id,
                "title": title,
                "budget": budget,
                "initial_events": initial_events,
                "metadata": metadata,
                "resources": resources,
                "vault_ids": vault_ids,
            },
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Session, options=options)

    def retrieve(
        self,
        session_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """GET /sessions/{session_id}."""
        _path = path_template("/sessions/{session_id}", session_id=session_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Session, options=options)

    def update(
        self,
        session_id: str,
        *,
        environment_variables: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        title: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        agent: Union[SessionAgentUpdateParam, None, NotGiven] = NOT_GIVEN,
        budget: Union[BudgetLimitParam, None, NotGiven] = NOT_GIVEN,
        vault_ids: Union[List[str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """POST /sessions/{session_id}."""
        _path = path_template("/sessions/{session_id}", session_id=session_id)
        options = make_request_options(
            body={
                "environment_variables": environment_variables,
                "title": title,
                "metadata": metadata,
                "agent": agent,
                "budget": budget,
                "vault_ids": vault_ids,
            },
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Session, options=options)

    def list(
        self,
        *,
        agent_id: Union[str, None, NotGiven] = NOT_GIVEN,
        agent_version: Union[int, None, NotGiven] = NOT_GIVEN,
        created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        deployment_id: Union[str, None, NotGiven] = NOT_GIVEN,
        include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        memory_store_id: Union[str, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], None, NotGiven] = NOT_GIVEN,
        statuses: Union[List[str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Session]:
        """GET /sessions."""
        _path = path_template("/sessions")
        options = make_request_options(
            body={},
            query={
                "agent_id": agent_id,
                "agent_version": agent_version,
                "created_at[gt]": created_at_gt,
                "created_at[gte]": created_at_gte,
                "created_at[lt]": created_at_lt,
                "created_at[lte]": created_at_lte,
                "deployment_id": deployment_id,
                "include_archived": include_archived,
                "limit": limit,
                "memory_store_id": memory_store_id,
                "page": page,
                "order": order,
                "statuses[]": statuses,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request(
            "GET", _path, cast_to=Session, options=options, page_style="BidirectionalPageCursor"
        )

    def delete(
        self,
        session_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedSession:
        """DELETE /sessions/{session_id}."""
        _path = path_template("/sessions/{session_id}", session_id=session_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("DELETE", _path, cast_to=DeletedSession, options=options)

    def archive(
        self,
        session_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """POST /sessions/{session_id}/archive."""
        _path = path_template("/sessions/{session_id}/archive", session_id=session_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Session, options=options)


class AsyncSessions(AsyncAPIResource):
    @cached_property
    def events(self) -> AsyncEvents:
        return AsyncEvents(self._client)

    @cached_property
    def resources(self) -> AsyncResources:
        return AsyncResources(self._client)

    @cached_property
    def threads(self) -> AsyncThreads:
        return AsyncThreads(self._client)

    async def create(
        self,
        *,
        agent: Union[str, AgentParams, AgentWithOverridesParams],
        environment_id: str,
        environment_variables: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        title: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        budget: Union[BudgetLimitParam, None, NotGiven] = NOT_GIVEN,
        initial_events: Union[
            List[Union[UserMessageEventParams, UserDefineOutcomeEventParams]], None, NotGiven
        ] = NOT_GIVEN,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        resources: Union[
            List[Union[GitHubRepositoryResourceParams, FileResourceParams, MemoryStoreResourceParam]], None, NotGiven
        ] = NOT_GIVEN,
        vault_ids: Union[List[str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """POST /sessions."""
        _path = path_template("/sessions")
        options = make_request_options(
            body={
                "environment_variables": environment_variables,
                "agent": agent,
                "environment_id": environment_id,
                "title": title,
                "budget": budget,
                "initial_events": initial_events,
                "metadata": metadata,
                "resources": resources,
                "vault_ids": vault_ids,
            },
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Session, options=options)

    async def retrieve(
        self,
        session_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """GET /sessions/{session_id}."""
        _path = path_template("/sessions/{session_id}", session_id=session_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=Session, options=options)

    async def update(
        self,
        session_id: str,
        *,
        environment_variables: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        title: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        agent: Union[SessionAgentUpdateParam, None, NotGiven] = NOT_GIVEN,
        budget: Union[BudgetLimitParam, None, NotGiven] = NOT_GIVEN,
        vault_ids: Union[List[str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """POST /sessions/{session_id}."""
        _path = path_template("/sessions/{session_id}", session_id=session_id)
        options = make_request_options(
            body={
                "environment_variables": environment_variables,
                "title": title,
                "metadata": metadata,
                "agent": agent,
                "budget": budget,
                "vault_ids": vault_ids,
            },
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Session, options=options)

    def list(
        self,
        *,
        agent_id: Union[str, None, NotGiven] = NOT_GIVEN,
        agent_version: Union[int, None, NotGiven] = NOT_GIVEN,
        created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        deployment_id: Union[str, None, NotGiven] = NOT_GIVEN,
        include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        memory_store_id: Union[str, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        order: Union[Literal["asc", "desc"], None, NotGiven] = NOT_GIVEN,
        statuses: Union[List[str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Session]:
        """GET /sessions."""
        _path = path_template("/sessions")
        options = make_request_options(
            body={},
            query={
                "agent_id": agent_id,
                "agent_version": agent_version,
                "created_at[gt]": created_at_gt,
                "created_at[gte]": created_at_gte,
                "created_at[lt]": created_at_lt,
                "created_at[lte]": created_at_lte,
                "deployment_id": deployment_id,
                "include_archived": include_archived,
                "limit": limit,
                "memory_store_id": memory_store_id,
                "page": page,
                "order": order,
                "statuses[]": statuses,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request(
                "GET", _path, cast_to=Session, options=options, page_style="BidirectionalPageCursor"
            )
        )

    async def delete(
        self,
        session_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedSession:
        """DELETE /sessions/{session_id}."""
        _path = path_template("/sessions/{session_id}", session_id=session_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("DELETE", _path, cast_to=DeletedSession, options=options)

    async def archive(
        self,
        session_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """POST /sessions/{session_id}/archive."""
        _path = path_template("/sessions/{session_id}/archive", session_id=session_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Session, options=options)
