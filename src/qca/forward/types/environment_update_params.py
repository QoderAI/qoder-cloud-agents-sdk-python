from __future__ import annotations

from typing import Any, Dict, Optional

from typing_extensions import TypedDict

__all__ = ["EnvironmentUpdateParams"]


class EnvironmentUpdateParams(TypedDict, total=False):
    name: Optional[str]
    description: Optional[str]
    config: Dict[str, Any]
    metadata: Dict[str, Any]
