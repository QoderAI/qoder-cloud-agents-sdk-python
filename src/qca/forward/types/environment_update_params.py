from __future__ import annotations

from typing import Any, Dict, Optional

from typing_extensions import TypedDict

__all__ = ["EnvironmentUpdateParams"]


class EnvironmentUpdateParams(TypedDict, total=False):
    identity_id: str
    """Select identity ownership with a PAT. Omit when using a SAT."""
    name: Optional[str]
    description: Optional[str]
    config: Dict[str, Any]
    metadata: Dict[str, Any]
