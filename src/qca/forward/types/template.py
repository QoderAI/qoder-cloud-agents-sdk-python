from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .git_hub_repository import GitHubRepository
    from .mcp_server import MCPServer
    from .model_config import ModelConfig
    from .multiagent_config import MultiagentConfig
    from .resource_binding import ResourceBinding
    from .skill_binding import SkillBinding
    from .tool import Tool

__all__ = ["Template"]


class Template(BaseModel):
    type: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    model: Optional[Union[str, ModelConfig]] = None
    multiagent: Optional[MultiagentConfig] = None
    environment_id: Optional[str] = None
    vaults: Optional[Dict[str, ResourceBinding]] = None
    files: Optional[Dict[str, ResourceBinding]] = None
    github_repositories: Optional[Dict[str, GitHubRepository]] = None
    system: Optional[str] = None
    tools: Optional[List[Tool]] = None
    mcp_servers: Optional[List[MCPServer]] = None
    skills: Optional[List[SkillBinding]] = None
    environment_variables: Optional[Dict[str, str]] = None
    metadata: Optional[Dict[str, Any]] = None
