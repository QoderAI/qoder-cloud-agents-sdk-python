from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["MemoryStoreListParams"]


class MemoryStoreListParams(TypedDict, total=False):
    limit: Optional[int]
    before_id: Optional[str]
    after_id: Optional[str]
    system_managed: Optional[bool]
