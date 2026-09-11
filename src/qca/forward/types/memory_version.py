from __future__ import annotations

from datetime import datetime
from typing import Any, Optional

from qca.common._models import BaseModel

__all__ = ["MemoryVersion"]


class MemoryVersion(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    memory_store_id: Optional[str] = None
    memory_id: Optional[str] = None
    path: Optional[str] = None
    content_size_bytes: Optional[int] = None
    content_sha256: Optional[str] = None
    operation: Optional[str] = None
    redacted: Optional[bool] = None
    redacted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    content: Optional[Any] = None
