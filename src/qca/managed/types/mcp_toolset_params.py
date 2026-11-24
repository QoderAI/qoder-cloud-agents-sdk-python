from __future__ import annotations

from typing import TYPE_CHECKING, List, Literal, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .always_allow_policy_param import AlwaysAllowPolicyParam
    from .always_ask_policy_param import AlwaysAskPolicyParam
    from .always_deny_policy_param import AlwaysDenyPolicyParam
    from .mcp_tool_config_params import MCPToolConfigParams
    from .mcp_toolset_default_config_params import MCPToolsetDefaultConfigParams

__all__ = ["MCPToolsetParams"]


class MCPToolsetParams(TypedDict, total=False):
    """MCP governance reads the server-wide policy from top-level permission_policy."""

    mcp_server_name: Required[str]
    type: Required[Literal["mcp_toolset"]]
    permission_policy: Union[AlwaysAllowPolicyParam, AlwaysAskPolicyParam, AlwaysDenyPolicyParam]
    """Server-wide default: always_allow, always_ask or always_deny; omission defaults to allow."""

    configs: List[MCPToolConfigParams]
    default_config: MCPToolsetDefaultConfigParams
    """Legacy payload compatibility only; nested permission_policy does not set the MCP default."""
