from __future__ import annotations

from typing import Literal, Optional

from qca.common._models import BaseModel

__all__ = ["DeletedSkillVersion"]


class DeletedSkillVersion(BaseModel):
    id: Optional[str] = None
    type: Optional[Literal["skill_version_deleted"]] = None
