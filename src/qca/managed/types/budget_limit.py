from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount

__all__ = ["BudgetLimit"]


class BudgetLimit(BaseModel):
    max_list_cost: Optional[MonetaryAmount] = None
    type: Optional[str] = None
