from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["ScheduleInitialEventsItem"]


class ScheduleInitialEventsItem(BaseModel):
    type: Optional[str] = None
    content: Optional[str] = None
