from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .agent_tool_config_union_permission_policy import AgentToolConfigUnionPermissionPolicy
    from .user_location import UserLocation

__all__ = ["AgentToolConfigUnion"]


class AgentToolConfigUnion(BaseModel):
    enabled: Optional[bool] = None
    name: Optional[str] = None
    permission_policy: Optional[AgentToolConfigUnionPermissionPolicy] = None
    type: Optional[str] = None
    allowed_domains: Optional[List[str]] = None
    blocked_domains: Optional[List[str]] = None
    max_content_tokens: Optional[int] = None
    user_location: Optional[UserLocation] = None
