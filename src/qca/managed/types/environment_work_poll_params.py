from __future__ import annotations

from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["EnvironmentWorkPollParams"]


class EnvironmentWorkPollParams(TypedDict, total=False):
    block_ms: Optional[int]
    reclaim_older_than_ms: Optional[int]
    worker_id: Optional[str]
    betas: List[str]
