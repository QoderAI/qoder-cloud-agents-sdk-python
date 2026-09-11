from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .permission_policy import PermissionPolicy

__all__ = ["ToolConfig"]


class ToolConfig(BaseModel):
    name: Optional[str] = None
    enabled: Optional[bool] = None
    permission_policy: Optional[PermissionPolicy] = None
