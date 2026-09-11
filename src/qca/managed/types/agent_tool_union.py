from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Union

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .agent_tool_config_union import AgentToolConfigUnion
    from .agent_tool_union_default_config import AgentToolUnionDefaultConfig
    from .custom_tool_input_schema import CustomToolInputSchema
    from .mcp_tool_config import MCPToolConfig

__all__ = ["AgentToolUnion"]


class AgentToolUnion(BaseModel):
    enabled_tools: Optional[List[str]] = None
    disallowed_tools: Optional[List[str]] = None
    configs: Optional[Union[List[AgentToolConfigUnion], List[MCPToolConfig]]] = None
    default_config: Optional[AgentToolUnionDefaultConfig] = None
    type: Optional[str] = None
    mcp_server_name: Optional[str] = None
    description: Optional[str] = None
    input_schema: Optional[CustomToolInputSchema] = None
    name: Optional[str] = None
