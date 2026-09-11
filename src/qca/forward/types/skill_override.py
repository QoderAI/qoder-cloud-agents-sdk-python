from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["SkillOverride"]


class SkillOverride(BaseModel):
    enabled: Optional[bool] = None
    type: Optional[str] = None
    version: Optional[str] = None
