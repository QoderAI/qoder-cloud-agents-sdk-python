from __future__ import annotations

from datetime import datetime
from functools import cached_property
from typing import Any, Dict, List, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.managed.resources.agents.versions import AsyncVersions, Versions
from qca.managed.types.agent import Agent
from qca.managed.types.agent_toolset20260401_params import AgentToolset20260401Params
from qca.managed.types.custom_skill_params import CustomSkillParams
from qca.managed.types.custom_tool_params import CustomToolParams
from qca.managed.types.mcp_toolset_params import MCPToolsetParams
from qca.managed.types.model_config_params import ModelConfigParams
from qca.managed.types.multiagent_params import MultiagentParams
from qca.managed.types.qoder_skill_params import QoderSkillParams
from qca.managed.types.urlmcp_server_params import URLMCPServerParams

__all__ = ["Agents", "AsyncAgents"]


class Agents(SyncAPIResource):
    @cached_property
    def versions(self) -> Versions:
        return Versions(self._client)

    def create(
        self,
        *,
        model: Union[str, ModelConfigParams],
        name: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        system: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        mcp_servers: Union[List[URLMCPServerParams], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        multiagent: Union[MultiagentParams, None, NotGiven] = NOT_GIVEN,
        skills: Union[List[Union[QoderSkillParams, CustomSkillParams]], None, NotGiven] = NOT_GIVEN,
        tools: Union[
            List[Union[AgentToolset20260401Params, MCPToolsetParams, CustomToolParams]], None, NotGiven
        ] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """POST /agents."""
        _path = path_template("/agents")
        options = make_request_options(
            body={
                "model": model,
                "name": name,
                "description": description,
                "system": system,
                "mcp_servers": mcp_servers,
                "metadata": metadata,
                "multiagent": multiagent,
                "skills": skills,
                "tools": tools,
            },
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Agent, options=options)

    def retrieve(
        self,
        agent_id: str,
        *,
        version: Union[int, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """GET /agents/{agent_id}."""
        _path = path_template("/agents/{agent_id}", agent_id=agent_id)
        options = make_request_options(
            body={},
            query={"version": version},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Agent, options=options)

    def update(
        self,
        agent_id: str,
        *,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        system: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        version: Union[int, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        mcp_servers: Union[List[URLMCPServerParams], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        skills: Union[List[Union[QoderSkillParams, CustomSkillParams]], None, NotGiven] = NOT_GIVEN,
        tools: Union[
            List[Union[AgentToolset20260401Params, MCPToolsetParams, CustomToolParams]], None, NotGiven
        ] = NOT_GIVEN,
        model: Union[Union[str, ModelConfigParams], None, NotGiven] = NOT_GIVEN,
        multiagent: Union[MultiagentParams, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """POST /agents/{agent_id}."""
        _path = path_template("/agents/{agent_id}", agent_id=agent_id)
        options = make_request_options(
            body={
                "description": description,
                "system": system,
                "name": name,
                "version": version,
                "mcp_servers": mcp_servers,
                "metadata": metadata,
                "skills": skills,
                "tools": tools,
                "model": model,
                "multiagent": multiagent,
            },
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Agent, options=options)

    def list(
        self,
        *,
        created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Agent]:
        """GET /agents."""
        _path = path_template("/agents")
        options = make_request_options(
            body={},
            query={
                "created_at[gte]": created_at_gte,
                "created_at[lte]": created_at_lte,
                "include_archived": include_archived,
                "limit": limit,
                "page": page,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Agent, options=options, page_style="PageCursor")

    def archive(
        self,
        agent_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """POST /agents/{agent_id}/archive."""
        _path = path_template("/agents/{agent_id}/archive", agent_id=agent_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Agent, options=options)


class AsyncAgents(AsyncAPIResource):
    @cached_property
    def versions(self) -> AsyncVersions:
        return AsyncVersions(self._client)

    async def create(
        self,
        *,
        model: Union[str, ModelConfigParams],
        name: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        system: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        mcp_servers: Union[List[URLMCPServerParams], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        multiagent: Union[MultiagentParams, None, NotGiven] = NOT_GIVEN,
        skills: Union[List[Union[QoderSkillParams, CustomSkillParams]], None, NotGiven] = NOT_GIVEN,
        tools: Union[
            List[Union[AgentToolset20260401Params, MCPToolsetParams, CustomToolParams]], None, NotGiven
        ] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """POST /agents."""
        _path = path_template("/agents")
        options = make_request_options(
            body={
                "model": model,
                "name": name,
                "description": description,
                "system": system,
                "mcp_servers": mcp_servers,
                "metadata": metadata,
                "multiagent": multiagent,
                "skills": skills,
                "tools": tools,
            },
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Agent, options=options)

    async def retrieve(
        self,
        agent_id: str,
        *,
        version: Union[int, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """GET /agents/{agent_id}."""
        _path = path_template("/agents/{agent_id}", agent_id=agent_id)
        options = make_request_options(
            body={},
            query={"version": version},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=Agent, options=options)

    async def update(
        self,
        agent_id: str,
        *,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        system: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        version: Union[int, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        mcp_servers: Union[List[URLMCPServerParams], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        skills: Union[List[Union[QoderSkillParams, CustomSkillParams]], None, NotGiven] = NOT_GIVEN,
        tools: Union[
            List[Union[AgentToolset20260401Params, MCPToolsetParams, CustomToolParams]], None, NotGiven
        ] = NOT_GIVEN,
        model: Union[Union[str, ModelConfigParams], None, NotGiven] = NOT_GIVEN,
        multiagent: Union[MultiagentParams, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """POST /agents/{agent_id}."""
        _path = path_template("/agents/{agent_id}", agent_id=agent_id)
        options = make_request_options(
            body={
                "description": description,
                "system": system,
                "name": name,
                "version": version,
                "mcp_servers": mcp_servers,
                "metadata": metadata,
                "skills": skills,
                "tools": tools,
                "model": model,
                "multiagent": multiagent,
            },
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Agent, options=options)

    def list(
        self,
        *,
        created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
        include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Agent]:
        """GET /agents."""
        _path = path_template("/agents")
        options = make_request_options(
            body={},
            query={
                "created_at[gte]": created_at_gte,
                "created_at[lte]": created_at_lte,
                "include_archived": include_archived,
                "limit": limit,
                "page": page,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=Agent, options=options, page_style="PageCursor")
        )

    async def archive(
        self,
        agent_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """POST /agents/{agent_id}/archive."""
        _path = path_template("/agents/{agent_id}/archive", agent_id=agent_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Agent, options=options)
