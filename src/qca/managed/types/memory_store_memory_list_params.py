from __future__ import annotations

from typing import List, Literal, Optional

from typing_extensions import TypedDict

__all__ = ["MemoryStoreMemoryListParams"]


class MemoryStoreMemoryListParams(TypedDict, total=False):
    depth: Optional[int]
    limit: Optional[int]
    page: Optional[str]
    path_prefix: Optional[str]
    workspace_id: Optional[str]
    view: Literal["basic", "full"]
    betas: List[str]
