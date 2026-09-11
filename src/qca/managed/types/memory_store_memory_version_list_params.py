from __future__ import annotations

from datetime import datetime
from typing import List, Literal, Optional

from typing_extensions import TypedDict

__all__ = ["MemoryStoreMemoryVersionListParams"]


class MemoryStoreMemoryVersionListParams(TypedDict, total=False):
    api_key_id: Optional[str]
    created_at_gte: Optional[datetime]
    created_at_lte: Optional[datetime]
    limit: Optional[int]
    memory_id: Optional[str]
    page: Optional[str]
    service_account_id: Optional[str]
    session_id: Optional[str]
    workspace_id: Optional[str]
    operation: Literal["created", "modified", "deleted"]
    view: Literal["basic", "full"]
    betas: List[str]
