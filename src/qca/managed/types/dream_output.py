from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["DreamOutput"]


class DreamOutput(BaseModel):
    memory_store_id: Optional[str] = None
    type: Optional[str] = None
