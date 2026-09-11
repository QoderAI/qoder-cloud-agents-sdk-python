from __future__ import annotations

from typing import List, Optional

from qca.common._models import BaseModel

__all__ = ["DreamInputUnion"]


class DreamInputUnion(BaseModel):
    memory_store_id: Optional[str] = None
    type: Optional[str] = None
    session_ids: Optional[List[str]] = None
