from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, Optional

from qca.common._models import BaseModel

__all__ = ["MemoryStore"]


class MemoryStore(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    entry_count: Optional[int] = None
    total_size: Optional[int] = None
    metadata: Optional[Dict[str, Any]] = None
    system_managed: Optional[bool] = None
    identity_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    archived_at: Optional[datetime] = None
    binding_info: Optional[Dict[str, int]] = None
