from __future__ import annotations

from typing import Any, Dict, Optional

from typing_extensions import Required, TypedDict

from .memory_store_create_mount_param import MemoryStoreCreateMountParam

__all__ = ["MemoryStoreCreateParams"]


class MemoryStoreCreateParams(TypedDict, total=False):
    mount: MemoryStoreCreateMountParam
    name: Required[str]
    description: Optional[str]
    metadata: Dict[str, Any]
    idempotency_key: Required[str]
