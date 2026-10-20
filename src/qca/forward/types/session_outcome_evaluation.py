from __future__ import annotations

from datetime import datetime
from typing import Optional

from qca.common._models import BaseModel

__all__ = ["SessionOutcomeEvaluation"]


class SessionOutcomeEvaluation(BaseModel):
    type: Optional[str] = None
    outcome_id: Optional[str] = None
    description: Optional[str] = None
    iteration: Optional[int] = None
    result: Optional[str] = None
    explanation: Optional[str] = None
    completed_at: Optional[datetime] = None
