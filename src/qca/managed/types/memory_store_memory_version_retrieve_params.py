from __future__ import annotations

from typing import List, Literal, Optional

from typing_extensions import TypedDict

__all__ = ["MemoryStoreMemoryVersionRetrieveParams"]


class MemoryStoreMemoryVersionRetrieveParams(TypedDict, total=False):
    workspace_id: Optional[str]
    view: Literal["basic", "full"]
    betas: List[str]
