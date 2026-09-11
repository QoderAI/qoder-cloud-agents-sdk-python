from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["MemoryStoreMemoryListParams"]


class MemoryStoreMemoryListParams(TypedDict, total=False):
    limit: Optional[int]
    before_id: Optional[str]
    after_id: Optional[str]
    path_prefix: Optional[str]
