from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .git_hub_repository_param import GitHubRepositoryParam
    from .managed_tool_config_param import ManagedToolConfigParam
    from .mcp_server_param import MCPServerParam
    from .model_config_param import ModelConfigParam
    from .multiagent_config_param import MultiagentConfigParam
    from .resource_binding_param import ResourceBindingParam
    from .skill_binding_param import SkillBindingParam
    from .tool_param import ToolParam

__all__ = ["TemplateCreateParams"]


class TemplateCreateParams(TypedDict, total=False):
    max_tool_rounds: Optional[int]
    managed_tool_config: Optional[ManagedToolConfigParam]
    name: Required[str]
    model: Required[Union[str, ModelConfigParam]]
    environment_id: Required[str]
    description: Optional[str]
    system: Optional[str]
    tools: List[ToolParam]
    mcp_servers: List[MCPServerParam]
    skills: List[SkillBindingParam]
    multiagent: MultiagentConfigParam
    vaults: Dict[str, ResourceBindingParam]
    files: Dict[str, ResourceBindingParam]
    github_repositories: Dict[str, GitHubRepositoryParam]
    environment_variables: Union[Dict[str, Any], str]
    metadata: Dict[str, Any]
    idempotency_key: Optional[str]
    beta: Optional[str]
