from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Union

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .agent_tool_config_union import AgentToolConfigUnion
    from .agent_tool_config_union_permission_policy import AgentToolConfigUnionPermissionPolicy
    from .custom_tool_input_schema import CustomToolInputSchema
    from .deliver_artifacts_tool_config import DeliverArtifactsToolConfig
    from .image_gen_tool_config import ImageGenToolConfig
    from .image_search_tool_config import ImageSearchToolConfig
    from .mcp_tool_config import MCPToolConfig
    from .session_thread_agent_tool_union_default_config import SessionThreadAgentToolUnionDefaultConfig
    from .video_gen_tool_config import VideoGenToolConfig

__all__ = ["SessionThreadAgentToolUnion"]


class SessionThreadAgentToolUnion(BaseModel):
    enabled_tools: Optional[List[str]] = None
    disallowed_tools: Optional[List[str]] = None
    configs: Optional[
        Union[
            List[
                Union[
                    ImageGenToolConfig,
                    ImageSearchToolConfig,
                    VideoGenToolConfig,
                    DeliverArtifactsToolConfig,
                    AgentToolConfigUnion,
                ]
            ],
            List[MCPToolConfig],
        ]
    ] = None
    default_config: Optional[SessionThreadAgentToolUnionDefaultConfig] = None
    type: Optional[str] = None
    mcp_server_name: Optional[str] = None
    permission_policy: Optional[AgentToolConfigUnionPermissionPolicy] = None
    """For MCP, the server-wide default is read from this top-level field, not default_config."""

    description: Optional[str] = None
    input_schema: Optional[CustomToolInputSchema] = None
    name: Optional[str] = None
