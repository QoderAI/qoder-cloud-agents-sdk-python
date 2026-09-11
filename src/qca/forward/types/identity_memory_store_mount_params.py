from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IdentityMemoryStoreMountParams"]


class IdentityMemoryStoreMountParams(TypedDict, total=False):
    memory_store_id: Required[str]
