from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .session_thread_agent_tool_union_default_config_permission_policy import (
        SessionThreadAgentToolUnionDefaultConfigPermissionPolicy,
    )

__all__ = ["SessionThreadAgentToolUnionDefaultConfig"]


class SessionThreadAgentToolUnionDefaultConfig(BaseModel):
    enabled: Optional[bool] = None
    permission_policy: Optional[SessionThreadAgentToolUnionDefaultConfigPermissionPolicy] = None
