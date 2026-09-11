from __future__ import annotations

from typing import Any, Dict, List, Optional

from typing_extensions import TypedDict

__all__ = ["MemoryStoreUpdateParams"]


class MemoryStoreUpdateParams(TypedDict, total=False):
    description: Optional[str]
    name: Optional[str]
    workspace_id: Optional[str]
    metadata: Dict[str, Any]
    betas: List[str]
