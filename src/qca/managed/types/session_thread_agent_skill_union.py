from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["SessionThreadAgentSkillUnion"]


class SessionThreadAgentSkillUnion(BaseModel):
    skill_id: Optional[str] = None
    type: Optional[str] = None
    version: Optional[str] = None
