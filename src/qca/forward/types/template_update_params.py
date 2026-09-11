from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from .git_hub_repository_param import GitHubRepositoryParam
    from .mcp_server_param import MCPServerParam
    from .model_config_param import ModelConfigParam
    from .multiagent_config_param import MultiagentConfigParam
    from .resource_binding_param import ResourceBindingParam
    from .skill_binding_param import SkillBindingParam
    from .tool_param import ToolParam

__all__ = ["TemplateUpdateParams"]


class TemplateUpdateParams(TypedDict, total=False):
    name: Optional[str]
    description: Optional[str]
    model: Union[str, ModelConfigParam]
    system: Optional[str]
    tools: List[ToolParam]
    mcp_servers: List[MCPServerParam]
    skills: List[SkillBindingParam]
    multiagent: MultiagentConfigParam
    environment_id: Optional[str]
    vaults: Dict[str, ResourceBindingParam]
    files: Dict[str, ResourceBindingParam]
    github_repositories: Dict[str, GitHubRepositoryParam]
    environment_variables: Union[Dict[str, Any], str]
    metadata: Dict[str, Any]
    idempotency_key: Optional[str]
    beta: Optional[str]
