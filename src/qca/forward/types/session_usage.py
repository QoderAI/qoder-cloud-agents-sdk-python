from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["SessionUsage"]


class SessionUsage(BaseModel):
    model_credits: Optional[float] = None
    sandbox_runtime_credits: Optional[float] = None
    total_credits: Optional[float] = None
