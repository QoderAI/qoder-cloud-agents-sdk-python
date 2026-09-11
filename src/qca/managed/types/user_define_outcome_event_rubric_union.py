from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["UserDefineOutcomeEventRubricUnion"]


class UserDefineOutcomeEventRubricUnion(BaseModel):
    file_id: Optional[str] = None
    type: Optional[str] = None
    content: Optional[str] = None
