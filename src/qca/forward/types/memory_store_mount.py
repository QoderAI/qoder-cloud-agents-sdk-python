from __future__ import annotations

from datetime import datetime
from typing import Optional

from qca.common._models import BaseModel

__all__ = ["MemoryStoreMount"]


class MemoryStoreMount(BaseModel):
    memory_store_id: Optional[str] = None
    identity_id: Optional[str] = None
    template_id: Optional[str] = None
    access: Optional[str] = None
    system_managed: Optional[bool] = None
    name: Optional[str] = None
    status: Optional[str] = None
    entry_count: Optional[int] = None
    created_at: Optional[datetime] = None
