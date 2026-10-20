from __future__ import annotations

from typing import Any, Dict, Optional

from typing_extensions import Required, TypedDict

__all__ = ["VaultCreateParams"]


class VaultCreateParams(TypedDict, total=False):
    identity_id: str
    """Select identity ownership with a PAT. Omit when using a SAT."""
    display_name: Required[str]
    metadata: Dict[str, Any]
    idempotency_key: Optional[str]
