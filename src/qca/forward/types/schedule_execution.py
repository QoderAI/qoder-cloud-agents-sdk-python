from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["ScheduleExecution"]


class ScheduleExecution(BaseModel):
    session_mode: Optional[str] = None
    max_concurrent_runs: Optional[int] = None
    max_attempts: Optional[int] = None
    timeout_ms: Optional[int] = None
