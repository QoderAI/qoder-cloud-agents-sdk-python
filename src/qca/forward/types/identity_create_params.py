from __future__ import annotations

from typing import Any, Dict, Optional

from typing_extensions import Required, TypedDict

__all__ = ["IdentityCreateParams"]


class IdentityCreateParams(TypedDict, total=False):
    external_id: Required[str]
    name: Optional[str]
    enabled: Optional[bool]
    metadata: Dict[str, Any]
    idempotency_key: Optional[str]
