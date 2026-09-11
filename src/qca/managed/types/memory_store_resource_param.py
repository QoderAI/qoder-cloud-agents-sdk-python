from __future__ import annotations

from typing import Literal, Optional

from typing_extensions import Required, TypedDict

__all__ = ["MemoryStoreResourceParam"]


class MemoryStoreResourceParam(TypedDict, total=False):
    memory_store_id: Required[str]
    type: Required[Literal["memory_store"]]
    instructions: Optional[str]
    access: Literal["read_write", "read_only"]
