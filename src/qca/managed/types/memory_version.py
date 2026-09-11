from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .actor_union import ActorUnion

__all__ = ["MemoryVersion"]


class MemoryVersion(BaseModel):
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    memory_id: Optional[str] = None
    memory_store_id: Optional[str] = None
    operation: Optional[str] = None
    type: Optional[str] = None
    content: Optional[str] = None
    content_sha256: Optional[str] = None
    content_size_bytes: Optional[int] = None
    created_by: Optional[ActorUnion] = None
    path: Optional[str] = None
    redacted_at: Optional[datetime] = None
    redacted_by: Optional[ActorUnion] = None
