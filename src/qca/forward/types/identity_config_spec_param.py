from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Union

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from .environment_variable_override_param import EnvironmentVariableOverrideParam
    from .git_hub_repository_param import GitHubRepositoryParam
    from .mcp_server_override_param import MCPServerOverrideParam
    from .model_config_param import ModelConfigParam
    from .resource_binding_param import ResourceBindingParam
    from .skill_override_param import SkillOverrideParam
    from .system_override_param import SystemOverrideParam
    from .tool_override_param import ToolOverrideParam

__all__ = ["IdentityConfigSpecParam"]


class IdentityConfigSpecParam(TypedDict, total=False):
    system: SystemOverrideParam
    model: Union[str, ModelConfigParam]
    tools: Dict[str, ToolOverrideParam]
    mcp_servers: Dict[str, MCPServerOverrideParam]
    skills: Dict[str, SkillOverrideParam]
    toolsets: Dict[str, Any]
    agent_metadata: Dict[str, Any]
    vaults: Dict[str, ResourceBindingParam]
    files: Dict[str, ResourceBindingParam]
    github_repositories: Dict[str, GitHubRepositoryParam]
    environment_variables: Dict[str, EnvironmentVariableOverrideParam]
