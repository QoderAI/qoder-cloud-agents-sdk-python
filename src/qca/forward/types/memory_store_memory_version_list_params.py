from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["MemoryStoreMemoryVersionListParams"]


class MemoryStoreMemoryVersionListParams(TypedDict, total=False):
    limit: Optional[int]
    before_id: Optional[str]
    after_id: Optional[str]
    memory_id: Optional[str]
