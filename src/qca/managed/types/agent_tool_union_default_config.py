from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .agent_tool_union_default_config_permission_policy import AgentToolUnionDefaultConfigPermissionPolicy

__all__ = ["AgentToolUnionDefaultConfig"]


class AgentToolUnionDefaultConfig(BaseModel):
    enabled: Optional[bool] = None
    permission_policy: Optional[AgentToolUnionDefaultConfigPermissionPolicy] = None
