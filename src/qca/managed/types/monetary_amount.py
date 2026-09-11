from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["MonetaryAmount"]


class MonetaryAmount(BaseModel):
    amount: Optional[str] = None
    currency: Optional[str] = None
