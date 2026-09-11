from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .environment_variable_override import EnvironmentVariableOverride
    from .git_hub_repository import GitHubRepository
    from .mcp_server_override import MCPServerOverride
    from .model_config import ModelConfig
    from .resource_binding import ResourceBinding
    from .skill_override import SkillOverride
    from .system_override import SystemOverride
    from .tool_override import ToolOverride

__all__ = ["IdentityConfigSpec"]


class IdentityConfigSpec(BaseModel):
    system: Optional[SystemOverride] = None
    model: Optional[Union[str, ModelConfig]] = None
    tools: Optional[Dict[str, ToolOverride]] = None
    mcp_servers: Optional[Dict[str, MCPServerOverride]] = None
    skills: Optional[Dict[str, SkillOverride]] = None
    toolsets: Optional[Dict[str, Any]] = None
    agent_metadata: Optional[Dict[str, Any]] = None
    vaults: Optional[Dict[str, ResourceBinding]] = None
    files: Optional[Dict[str, ResourceBinding]] = None
    github_repositories: Optional[Dict[str, GitHubRepository]] = None
    environment_variables: Optional[Dict[str, EnvironmentVariableOverride]] = None
