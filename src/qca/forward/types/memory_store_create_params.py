from __future__ import annotations

from typing import Any, Dict, Optional

from typing_extensions import Required, TypedDict

__all__ = ["MemoryStoreCreateParams"]


class MemoryStoreCreateParams(TypedDict, total=False):
    name: Required[str]
    description: Optional[str]
    metadata: Dict[str, Any]
    idempotency_key: Required[str]
