from __future__ import annotations

from typing import Any, Dict

from typing_extensions import Required, TypedDict

__all__ = ["MemoryStoreMemoryCreateParams"]


class MemoryStoreMemoryCreateParams(TypedDict, total=False):
    path: Required[str]
    content: Required[str]
    metadata: Dict[str, Any]
