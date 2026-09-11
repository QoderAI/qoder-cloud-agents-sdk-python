from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from .agent_toolset20260401_params import AgentToolset20260401Params
    from .custom_skill_params import CustomSkillParams
    from .custom_tool_params import CustomToolParams
    from .mcp_toolset_params import MCPToolsetParams
    from .model_config_params import ModelConfigParams
    from .multiagent_params import MultiagentParams
    from .qoder_skill_params import QoderSkillParams
    from .urlmcp_server_params import URLMCPServerParams

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
    description: Optional[str]
    system: Optional[str]
    name: Optional[str]
    version: Optional[int]
    workspace_id: Optional[str]
    mcp_servers: List[URLMCPServerParams]
    metadata: Dict[str, Any]
    skills: List[Union[QoderSkillParams, CustomSkillParams]]
    tools: List[Union[AgentToolset20260401Params, MCPToolsetParams, CustomToolParams]]
    model: Union[str, ModelConfigParams]
    multiagent: MultiagentParams
    betas: List[str]
