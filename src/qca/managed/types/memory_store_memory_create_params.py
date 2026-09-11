from __future__ import annotations

from typing import Dict, List, Literal, Optional

from typing_extensions import Required, TypedDict

__all__ = ["MemoryStoreMemoryCreateParams"]


class MemoryStoreMemoryCreateParams(TypedDict, total=False):
    metadata: Dict[str, str]
    content: Required[Optional[str]]
    path: Required[str]
    workspace_id: Optional[str]
    view: Literal["basic", "full"]
    betas: List[str]
