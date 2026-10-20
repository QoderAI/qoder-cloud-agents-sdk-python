from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["MemoryStoreCreateMountParam"]


class MemoryStoreCreateMountParam(TypedDict, total=False):
    identity_id: Required[str]
    template_id: Required[str]
    access: Literal["read_only", "read_write"]
