from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from qca.common._models import BaseModel

__all__ = ["Schedule"]


class Schedule(BaseModel):
    expression: Optional[str] = None
    timezone: Optional[str] = None
    type: Optional[str] = None
    last_run_at: Optional[datetime] = None
    upcoming_runs_at: Optional[List[datetime]] = None
