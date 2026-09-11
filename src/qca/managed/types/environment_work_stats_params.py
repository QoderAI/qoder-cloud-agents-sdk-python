from __future__ import annotations

from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["EnvironmentWorkStatsParams"]


class EnvironmentWorkStatsParams(TypedDict, total=False):
    workspace_id: Optional[str]
    betas: List[str]
