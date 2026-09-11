from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Union

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .agent_tool_config_union import AgentToolConfigUnion
    from .custom_tool_input_schema import CustomToolInputSchema
    from .mcp_tool_config import MCPToolConfig
    from .session_thread_agent_tool_union_default_config import SessionThreadAgentToolUnionDefaultConfig

__all__ = ["SessionThreadAgentToolUnion"]


class SessionThreadAgentToolUnion(BaseModel):
    enabled_tools: Optional[List[str]] = None
    disallowed_tools: Optional[List[str]] = None
    configs: Optional[Union[List[AgentToolConfigUnion], List[MCPToolConfig]]] = None
    default_config: Optional[SessionThreadAgentToolUnionDefaultConfig] = None
    type: Optional[str] = None
    mcp_server_name: Optional[str] = None
    description: Optional[str] = None
    input_schema: Optional[CustomToolInputSchema] = None
    name: Optional[str] = None
