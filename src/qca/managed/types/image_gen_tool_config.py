from __future__ import annotations

from typing import Literal, Optional

from qca.common._models import BaseModel

from .agent_tool_config_union_permission_policy import AgentToolConfigUnionPermissionPolicy

__all__ = ["ImageGenToolConfig"]


class ImageGenToolConfig(BaseModel):
    name: Literal["ImageGen", "image_gen"]
    enabled: Optional[bool] = None
    permission_policy: Optional[AgentToolConfigUnionPermissionPolicy] = None
