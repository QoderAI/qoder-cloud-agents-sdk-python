from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .session_agent_tool_union_default_config_permission_policy import (
        SessionAgentToolUnionDefaultConfigPermissionPolicy,
    )

__all__ = ["SessionAgentToolUnionDefaultConfig"]


class SessionAgentToolUnionDefaultConfig(BaseModel):
    enabled: Optional[bool] = None
    permission_policy: Optional[SessionAgentToolUnionDefaultConfigPermissionPolicy] = None
