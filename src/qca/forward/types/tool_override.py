from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .permission_policy import PermissionPolicy

__all__ = ["ToolOverride"]


class ToolOverride(BaseModel):
    enabled: Optional[bool] = None
    permission_policy: Optional[PermissionPolicy] = None
