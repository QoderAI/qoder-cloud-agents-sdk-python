from __future__ import annotations

from datetime import datetime
from typing import Optional

from qca.common._models import BaseModel

__all__ = ["ScheduleRunTriggerContext"]


class ScheduleRunTriggerContext(BaseModel):
    type: Optional[str] = None
    scheduled_at: Optional[datetime] = None
