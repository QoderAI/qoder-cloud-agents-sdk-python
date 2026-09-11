from __future__ import annotations

from typing import Any, Dict, List, Optional

from typing_extensions import Required, TypedDict

__all__ = ["EnvironmentWorkUpdateParams"]


class EnvironmentWorkUpdateParams(TypedDict, total=False):
    metadata: Required[Dict[str, Any]]
    workspace_id: Optional[str]
    betas: List[str]
