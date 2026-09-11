from __future__ import annotations

from typing import Any, Dict, Optional

from typing_extensions import Required, TypedDict

__all__ = ["MemoryStoreMemoryUpdateParams"]


class MemoryStoreMemoryUpdateParams(TypedDict, total=False):
    content: Required[str]
    content_sha256: Optional[str]
    metadata: Dict[str, Any]
