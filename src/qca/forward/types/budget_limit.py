from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["BudgetLimit"]


class BudgetLimit(BaseModel):
    # Positive decimal Credits, at most 12 integer and 2 fractional digits.
    max_credit_cost: Optional[str] = None
    type: Optional[str] = None
