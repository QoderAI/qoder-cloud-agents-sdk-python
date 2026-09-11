from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .mcp_tool_config_permission_policy_union import MCPToolConfigPermissionPolicyUnion

__all__ = ["MCPToolConfig"]


class MCPToolConfig(BaseModel):
    enabled: Optional[bool] = None
    name: Optional[str] = None
    permission_policy: Optional[MCPToolConfigPermissionPolicyUnion] = None
