from __future__ import annotations

from datetime import datetime
from typing import Literal, Optional

from qca.common._models import BaseModel

__all__ = ["SkillVersion"]


class SkillVersion(BaseModel):
    version: Optional[str] = None
    directory: Optional[str] = None
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    description: Optional[str] = None
    name: Optional[str] = None
    skill_id: Optional[str] = None
    type: Optional[Literal["skill_version"]] = None
