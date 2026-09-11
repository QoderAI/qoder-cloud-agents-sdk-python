from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["SkillBinding"]


class SkillBinding(BaseModel):
    type: Optional[str] = None
    skill_id: Optional[str] = None
    version: Optional[str] = None
    enabled: Optional[bool] = None
