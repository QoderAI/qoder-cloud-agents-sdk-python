from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Union

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .mcp_server_url_definition import MCPServerURLDefinition
    from .model_config import ModelConfig
    from .session_agent_skill_union import SessionAgentSkillUnion
    from .session_agent_tool_union import SessionAgentToolUnion
    from .session_multiagent_coordinator import SessionMultiagentCoordinator

__all__ = ["SessionAgent"]


class SessionAgent(BaseModel):
    id: Optional[str] = None
    description: Optional[str] = None
    mcp_servers: Optional[List[MCPServerURLDefinition]] = None
    model: Optional[Union[str, ModelConfig]] = None
    multiagent: Optional[SessionMultiagentCoordinator] = None
    name: Optional[str] = None
    skills: Optional[List[SessionAgentSkillUnion]] = None
    system: Optional[str] = None
    tools: Optional[List[SessionAgentToolUnion]] = None
    type: Optional[str] = None
    version: Optional[int] = None
