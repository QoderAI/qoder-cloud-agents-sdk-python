from __future__ import annotations

from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["EnvironmentWorkStopParams"]


class EnvironmentWorkStopParams(TypedDict, total=False):
    force: Optional[bool]
    workspace_id: Optional[str]
    betas: List[str]
