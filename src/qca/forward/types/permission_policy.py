from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["PermissionPolicy"]


class PermissionPolicy(BaseModel):
    type: Optional[str] = None
