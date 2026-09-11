from __future__ import annotations

from typing import TYPE_CHECKING, List, Literal

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .mcp_tool_config_params import MCPToolConfigParams
    from .mcp_toolset_default_config_params import MCPToolsetDefaultConfigParams

__all__ = ["MCPToolsetParams"]


class MCPToolsetParams(TypedDict, total=False):
    mcp_server_name: Required[str]
    type: Required[Literal["mcp_toolset"]]
    configs: List[MCPToolConfigParams]
    default_config: MCPToolsetDefaultConfigParams
