from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from qca.common._models import BaseModel

__all__ = ["ScheduleTriggerPolicy"]


class ScheduleTriggerPolicy(BaseModel):
    type: Optional[str] = None
    expression: Optional[str] = None
    timezone: Optional[str] = None
    upcoming_runs_at: Optional[List[datetime]] = None
