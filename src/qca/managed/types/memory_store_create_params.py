from __future__ import annotations

from typing import Dict, List, Optional

from typing_extensions import Required, TypedDict

__all__ = ["MemoryStoreCreateParams"]


class MemoryStoreCreateParams(TypedDict, total=False):
    name: Required[str]
    description: Optional[str]
    workspace_id: Optional[str]
    metadata: Dict[str, str]
    betas: List[str]
