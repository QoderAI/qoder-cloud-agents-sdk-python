from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .memory_store_mount import MemoryStoreMount

__all__ = ["IdentityMemoryStoreListResponse"]


class IdentityMemoryStoreListResponse(BaseModel):
    data: Optional[List[MemoryStoreMount]] = None
    has_more: Optional[bool] = None
