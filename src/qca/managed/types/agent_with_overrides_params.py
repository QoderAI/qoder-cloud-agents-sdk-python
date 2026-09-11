from __future__ import annotations

from typing import TYPE_CHECKING, List, Literal, Optional, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .agent_toolset20260401_params import AgentToolset20260401Params
    from .custom_skill_params import CustomSkillParams
    from .custom_tool_params import CustomToolParams
    from .mcp_toolset_params import MCPToolsetParams
    from .model_config_params import ModelConfigParams
    from .qoder_skill_params import QoderSkillParams
    from .urlmcp_server_params import URLMCPServerParams

__all__ = ["AgentWithOverridesParams"]


class AgentWithOverridesParams(TypedDict, total=False):
    id: Required[str]
    type: Required[Literal["agent_with_overrides"]]
    system: Optional[str]
    version: Optional[int]
    mcp_servers: List[URLMCPServerParams]
    model: Union[str, ModelConfigParams]
    skills: List[Union[QoderSkillParams, CustomSkillParams]]
    tools: List[Union[AgentToolset20260401Params, MCPToolsetParams, CustomToolParams]]
