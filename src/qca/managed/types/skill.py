from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Dict, Literal, Optional, Union

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .skill_source import SkillSource

__all__ = ["Skill"]


class Skill(BaseModel):
    metadata: Optional[Dict[str, str]] = None
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    display_title: Optional[str] = None
    latest_version: Optional[str] = None
    source: Optional[Union[str, SkillSource]] = None
    type: Optional[Literal["skill"]] = None
    updated_at: Optional[datetime] = None
