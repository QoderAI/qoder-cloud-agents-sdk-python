from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Union

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from .always_allow_policy_param import AlwaysAllowPolicyParam
    from .always_ask_policy_param import AlwaysAskPolicyParam
    from .always_deny_policy_param import AlwaysDenyPolicyParam

__all__ = ["MCPToolsetDefaultConfigParams"]


class MCPToolsetDefaultConfigParams(TypedDict, total=False):
    """Legacy payload compatibility; MCP defaults use the toolset's top-level permission_policy."""

    enabled: Optional[bool]
    permission_policy: Union[AlwaysAllowPolicyParam, AlwaysAskPolicyParam, AlwaysDenyPolicyParam]
    """Retained as-is; this nested field does not set the MCP server-wide policy."""
