from __future__ import annotations

from datetime import datetime
from typing import Optional

from qca.common._models import BaseModel

__all__ = ["MemoryListItemUnion"]


class MemoryListItemUnion(BaseModel):
    id: Optional[str] = None
    content_sha256: Optional[str] = None
    content_size_bytes: Optional[int] = None
    created_at: Optional[datetime] = None
    memory_store_id: Optional[str] = None
    memory_version_id: Optional[str] = None
    path: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[datetime] = None
    content: Optional[str] = None
