from __future__ import annotations

from datetime import datetime
from typing import Optional

from qca.common._models import BaseModel

__all__ = ["OutcomeEvaluationResource"]


class OutcomeEvaluationResource(BaseModel):
    completed_at: Optional[datetime] = None
    description: Optional[str] = None
    explanation: Optional[str] = None
    iteration: Optional[int] = None
    outcome_id: Optional[str] = None
    result: Optional[str] = None
    type: Optional[str] = None
