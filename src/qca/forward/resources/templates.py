from __future__ import annotations

from typing import Any, Dict, List, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.types.git_hub_repository_param import GitHubRepositoryParam
from qca.forward.types.mcp_server_param import MCPServerParam
from qca.forward.types.model_config_param import ModelConfigParam
from qca.forward.types.multiagent_config_param import MultiagentConfigParam
from qca.forward.types.resource_binding_param import ResourceBindingParam
from qca.forward.types.skill_binding_param import SkillBindingParam
from qca.forward.types.template import Template
from qca.forward.types.tool_param import ToolParam

__all__ = ["Templates", "AsyncTemplates"]


class Templates(SyncAPIResource):
    def list(
        self,
        *,
        status: Union[str, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Template]:
        """GET /templates."""
        _path = path_template("/templates")
        options = make_request_options(
            body={},
            query={"status": status, "limit": limit, "after_id": after_id, "before_id": before_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Template, options=options, page_style="Page")

    def create(
        self,
        *,
        name: str,
        model: Union[str, ModelConfigParam],
        environment_id: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        system: Union[str, None, NotGiven] = NOT_GIVEN,
        tools: Union[List[ToolParam], None, NotGiven] = NOT_GIVEN,
        mcp_servers: Union[List[MCPServerParam], None, NotGiven] = NOT_GIVEN,
        skills: Union[List[SkillBindingParam], None, NotGiven] = NOT_GIVEN,
        multiagent: Union[MultiagentConfigParam, None, NotGiven] = NOT_GIVEN,
        vaults: Union[Dict[str, ResourceBindingParam], None, NotGiven] = NOT_GIVEN,
        files: Union[Dict[str, ResourceBindingParam], None, NotGiven] = NOT_GIVEN,
        github_repositories: Union[Dict[str, GitHubRepositoryParam], None, NotGiven] = NOT_GIVEN,
        environment_variables: Union[Union[Dict[str, Any], str], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        beta: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Template:
        """POST /templates."""
        _path = path_template("/templates")
        options = make_request_options(
            body={
                "name": name,
                "model": model,
                "environment_id": environment_id,
                "description": description,
                "system": system,
                "tools": tools,
                "mcp_servers": mcp_servers,
                "skills": skills,
                "multiagent": multiagent,
                "vaults": vaults,
                "files": files,
                "github_repositories": github_repositories,
                "environment_variables": environment_variables,
                "metadata": metadata,
            },
            query={},
            headers={"Idempotency-Key": idempotency_key, "X-Qoder-Beta": beta},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Template, options=options)

    def retrieve(
        self,
        template_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Template:
        """GET /templates/{template_id}."""
        _path = path_template("/templates/{template_id}", template_id=template_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Template, options=options)

    def update(
        self,
        template_id: str,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        model: Union[Union[str, ModelConfigParam], None, NotGiven] = NOT_GIVEN,
        system: Union[str, None, NotGiven] = NOT_GIVEN,
        tools: Union[List[ToolParam], None, NotGiven] = NOT_GIVEN,
        mcp_servers: Union[List[MCPServerParam], None, NotGiven] = NOT_GIVEN,
        skills: Union[List[SkillBindingParam], None, NotGiven] = NOT_GIVEN,
        multiagent: Union[MultiagentConfigParam, None, NotGiven] = NOT_GIVEN,
        environment_id: Union[str, None, NotGiven] = NOT_GIVEN,
        vaults: Union[Dict[str, ResourceBindingParam], None, NotGiven] = NOT_GIVEN,
        files: Union[Dict[str, ResourceBindingParam], None, NotGiven] = NOT_GIVEN,
        github_repositories: Union[Dict[str, GitHubRepositoryParam], None, NotGiven] = NOT_GIVEN,
        environment_variables: Union[Union[Dict[str, Any], str], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        beta: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Template:
        """POST /templates/{template_id}."""
        _path = path_template("/templates/{template_id}", template_id=template_id)
        options = make_request_options(
            body={
                "name": name,
                "description": description,
                "model": model,
                "system": system,
                "tools": tools,
                "mcp_servers": mcp_servers,
                "skills": skills,
                "multiagent": multiagent,
                "environment_id": environment_id,
                "vaults": vaults,
                "files": files,
                "github_repositories": github_repositories,
                "environment_variables": environment_variables,
                "metadata": metadata,
            },
            query={},
            headers={"Idempotency-Key": idempotency_key, "X-Qoder-Beta": beta},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Template, options=options)

    def archive(
        self,
        template_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Template:
        """POST /templates/{template_id}/archive."""
        _path = path_template("/templates/{template_id}/archive", template_id=template_id)
        options = make_request_options(
            body={},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Template, options=options)

    def clone(
        self,
        template_id: str,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Template:
        """POST /templates/{template_id}/clone."""
        _path = path_template("/templates/{template_id}/clone", template_id=template_id)
        options = make_request_options(
            body={"name": name, "description": description},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Template, options=options)


class AsyncTemplates(AsyncAPIResource):
    def list(
        self,
        *,
        status: Union[str, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Template]:
        """GET /templates."""
        _path = path_template("/templates")
        options = make_request_options(
            body={},
            query={"status": status, "limit": limit, "after_id": after_id, "before_id": before_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=Template, options=options, page_style="Page")
        )

    async def create(
        self,
        *,
        name: str,
        model: Union[str, ModelConfigParam],
        environment_id: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        system: Union[str, None, NotGiven] = NOT_GIVEN,
        tools: Union[List[ToolParam], None, NotGiven] = NOT_GIVEN,
        mcp_servers: Union[List[MCPServerParam], None, NotGiven] = NOT_GIVEN,
        skills: Union[List[SkillBindingParam], None, NotGiven] = NOT_GIVEN,
        multiagent: Union[MultiagentConfigParam, None, NotGiven] = NOT_GIVEN,
        vaults: Union[Dict[str, ResourceBindingParam], None, NotGiven] = NOT_GIVEN,
        files: Union[Dict[str, ResourceBindingParam], None, NotGiven] = NOT_GIVEN,
        github_repositories: Union[Dict[str, GitHubRepositoryParam], None, NotGiven] = NOT_GIVEN,
        environment_variables: Union[Union[Dict[str, Any], str], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        beta: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Template:
        """POST /templates."""
        _path = path_template("/templates")
        options = make_request_options(
            body={
                "name": name,
                "model": model,
                "environment_id": environment_id,
                "description": description,
                "system": system,
                "tools": tools,
                "mcp_servers": mcp_servers,
                "skills": skills,
                "multiagent": multiagent,
                "vaults": vaults,
                "files": files,
                "github_repositories": github_repositories,
                "environment_variables": environment_variables,
                "metadata": metadata,
            },
            query={},
            headers={"Idempotency-Key": idempotency_key, "X-Qoder-Beta": beta},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Template, options=options)

    async def retrieve(
        self,
        template_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Template:
        """GET /templates/{template_id}."""
        _path = path_template("/templates/{template_id}", template_id=template_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=Template, options=options)

    async def update(
        self,
        template_id: str,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        model: Union[Union[str, ModelConfigParam], None, NotGiven] = NOT_GIVEN,
        system: Union[str, None, NotGiven] = NOT_GIVEN,
        tools: Union[List[ToolParam], None, NotGiven] = NOT_GIVEN,
        mcp_servers: Union[List[MCPServerParam], None, NotGiven] = NOT_GIVEN,
        skills: Union[List[SkillBindingParam], None, NotGiven] = NOT_GIVEN,
        multiagent: Union[MultiagentConfigParam, None, NotGiven] = NOT_GIVEN,
        environment_id: Union[str, None, NotGiven] = NOT_GIVEN,
        vaults: Union[Dict[str, ResourceBindingParam], None, NotGiven] = NOT_GIVEN,
        files: Union[Dict[str, ResourceBindingParam], None, NotGiven] = NOT_GIVEN,
        github_repositories: Union[Dict[str, GitHubRepositoryParam], None, NotGiven] = NOT_GIVEN,
        environment_variables: Union[Union[Dict[str, Any], str], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        beta: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Template:
        """POST /templates/{template_id}."""
        _path = path_template("/templates/{template_id}", template_id=template_id)
        options = make_request_options(
            body={
                "name": name,
                "description": description,
                "model": model,
                "system": system,
                "tools": tools,
                "mcp_servers": mcp_servers,
                "skills": skills,
                "multiagent": multiagent,
                "environment_id": environment_id,
                "vaults": vaults,
                "files": files,
                "github_repositories": github_repositories,
                "environment_variables": environment_variables,
                "metadata": metadata,
            },
            query={},
            headers={"Idempotency-Key": idempotency_key, "X-Qoder-Beta": beta},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Template, options=options)

    async def archive(
        self,
        template_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Template:
        """POST /templates/{template_id}/archive."""
        _path = path_template("/templates/{template_id}/archive", template_id=template_id)
        options = make_request_options(
            body={},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Template, options=options)

    async def clone(
        self,
        template_id: str,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Template:
        """POST /templates/{template_id}/clone."""
        _path = path_template("/templates/{template_id}/clone", template_id=template_id)
        options = make_request_options(
            body={"name": name, "description": description},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Template, options=options)
