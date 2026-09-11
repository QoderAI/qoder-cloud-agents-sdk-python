from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, Optional

from qca.common._models import BaseModel

__all__ = ["Memory"]


class Memory(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    memory_store_id: Optional[str] = None
    path: Optional[str] = None
    content_size_bytes: Optional[int] = None
    content_sha256: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    content: Optional[str] = None
