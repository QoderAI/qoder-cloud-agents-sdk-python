from __future__ import annotations

from datetime import datetime
from typing import Dict, Optional

from qca.common._models import BaseModel

__all__ = ["MemoryStore"]


class MemoryStore(BaseModel):
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    name: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[datetime] = None
    archived_at: Optional[datetime] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None
