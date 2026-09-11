from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Dict, List, Optional, Union

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .agent_skill_union import AgentSkillUnion
    from .agent_tool_union import AgentToolUnion
    from .mcp_server_url_definition import MCPServerURLDefinition
    from .model_config import ModelConfig
    from .multiagent import Multiagent

__all__ = ["Agent"]


class Agent(BaseModel):
    id: Optional[str] = None
    archived_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    description: Optional[str] = None
    mcp_servers: Optional[List[MCPServerURLDefinition]] = None
    metadata: Optional[Dict[str, str]] = None
    model: Optional[Union[str, ModelConfig]] = None
    multiagent: Optional[Multiagent] = None
    name: Optional[str] = None
    skills: Optional[List[AgentSkillUnion]] = None
    system: Optional[str] = None
    tools: Optional[List[AgentToolUnion]] = None
    type: Optional[str] = None
    updated_at: Optional[datetime] = None
    version: Optional[int] = None
