from __future__ import annotations

from typing import Any, Dict, Optional

from typing_extensions import TypedDict

__all__ = ["MemoryStoreUpdateParams"]


class MemoryStoreUpdateParams(TypedDict, total=False):
    name: Optional[str]
    description: Optional[str]
    metadata: Dict[str, Any]
