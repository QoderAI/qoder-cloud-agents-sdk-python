from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Union

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .mcp_server_url_definition import MCPServerURLDefinition
    from .model_config import ModelConfig
    from .session_thread_agent_skill_union import SessionThreadAgentSkillUnion
    from .session_thread_agent_tool_union import SessionThreadAgentToolUnion

__all__ = ["SessionMultiagentCoordinatorAgentUnion"]


class SessionMultiagentCoordinatorAgentUnion(BaseModel):
    id: Optional[str] = None
    description: Optional[str] = None
    mcp_servers: Optional[List[MCPServerURLDefinition]] = None
    model: Optional[Union[str, ModelConfig]] = None
    name: Optional[str] = None
    skills: Optional[List[SessionThreadAgentSkillUnion]] = None
    system: Optional[str] = None
    tools: Optional[List[SessionThreadAgentToolUnion]] = None
    type: Optional[str] = None
    version: Optional[int] = None
