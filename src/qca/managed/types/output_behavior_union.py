from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["OutputBehaviorUnion"]


class OutputBehaviorUnion(BaseModel):
    type: Optional[str] = None
    memory_store_id: Optional[str] = None
