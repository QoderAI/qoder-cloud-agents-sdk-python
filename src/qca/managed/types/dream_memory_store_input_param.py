from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["DreamMemoryStoreInputParam"]


class DreamMemoryStoreInputParam(TypedDict, total=False):
    memory_store_id: Required[str]
    type: Required[Literal["memory_store"]]
