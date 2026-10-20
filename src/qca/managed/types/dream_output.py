from __future__ import annotations

from typing import List, Optional

from qca.common._models import BaseModel

__all__ = ["DreamOutput"]


class DreamOutput(BaseModel):
    files_touched: Optional[List[str]] = None
    memory_store_id: Optional[str] = None
    type: Optional[str] = None
