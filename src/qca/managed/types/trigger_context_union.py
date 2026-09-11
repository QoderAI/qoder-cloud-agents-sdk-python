from __future__ import annotations

from datetime import datetime
from typing import Optional

from qca.common._models import BaseModel

__all__ = ["TriggerContextUnion"]


class TriggerContextUnion(BaseModel):
    scheduled_at: Optional[datetime] = None
    type: Optional[str] = None
