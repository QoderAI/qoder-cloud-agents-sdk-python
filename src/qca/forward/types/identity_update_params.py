from __future__ import annotations

from typing import Any, Dict, Optional

from typing_extensions import TypedDict

__all__ = ["IdentityUpdateParams"]


class IdentityUpdateParams(TypedDict, total=False):
    external_id: Optional[str]
    name: Optional[str]
    enabled: Optional[bool]
    metadata: Dict[str, Any]
    idempotency_key: Optional[str]
