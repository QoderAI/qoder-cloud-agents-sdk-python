from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["ScheduleSinksItemTarget"]


class ScheduleSinksItemTarget(BaseModel):
    type: Optional[str] = None
    external_id: Optional[str] = None
