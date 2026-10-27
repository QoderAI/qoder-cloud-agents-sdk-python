from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["IdentityMemoryStoreMountParams"]


class IdentityMemoryStoreMountParams(TypedDict, total=False):
    access: Literal["read_only", "read_write"]
    memory_store_id: Required[str]
