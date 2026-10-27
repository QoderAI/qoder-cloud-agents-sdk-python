from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from .environment_variable_override_param import EnvironmentVariableOverrideParam
    from .git_hub_repository_param import GitHubRepositoryParam
    from .managed_capability_override import ManagedCapabilityOverrideParam
    from .mcp_server_override_param import MCPServerOverrideParam
    from .model_config_param import ModelConfigParam
    from .resource_binding_param import ResourceBindingParam
    from .skill_override_param import SkillOverrideParam
    from .system_override_param import SystemOverrideParam
    from .tool_override_param import ToolOverrideParam
    from .tool_param import ToolParam

__all__ = ["IdentityConfigSpecParam"]


class IdentityConfigSpecParam(TypedDict, total=False):
    managed_tool_config: Optional[Dict[str, Optional[ManagedCapabilityOverrideParam]]]
    system: Optional[SystemOverrideParam]
    model: Optional[Union[str, ModelConfigParam]]
    tools: Optional[Union[Dict[str, Optional[ToolOverrideParam]], List[ToolParam]]]
    mcp_servers: Optional[Dict[str, MCPServerOverrideParam]]
    skills: Optional[Dict[str, SkillOverrideParam]]
    toolsets: Optional[Dict[str, Any]]
    agent_metadata: Optional[Dict[str, Any]]
    vaults: Optional[Dict[str, ResourceBindingParam]]
    files: Optional[Dict[str, ResourceBindingParam]]
    github_repositories: Optional[Dict[str, GitHubRepositoryParam]]
    environment_variables: Optional[Dict[str, EnvironmentVariableOverrideParam]]
