from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Union

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from .agent_toolset20260401_params import AgentToolset20260401Params
    from .custom_skill_params import CustomSkillParams
    from .custom_tool_params import CustomToolParams
    from .mcp_toolset_params import MCPToolsetParams
    from .model_config_params import ModelConfigParams
    from .qoder_skill_params import QoderSkillParams
    from .urlmcp_server_params import URLMCPServerParams

__all__ = ["SessionAgentUpdateParam"]


class SessionAgentUpdateParam(TypedDict, total=False):
    model: Union[str, ModelConfigParams]
    system: Optional[str]
    skills: List[Union[QoderSkillParams, CustomSkillParams]]
    mcp_servers: List[URLMCPServerParams]
    tools: List[Union[AgentToolset20260401Params, MCPToolsetParams, CustomToolParams]]
