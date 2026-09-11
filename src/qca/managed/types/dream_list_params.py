from __future__ import annotations

from datetime import datetime
from typing import List, Literal, Optional

from typing_extensions import TypedDict

__all__ = ["DreamListParams"]


class DreamListParams(TypedDict, total=False):
    created_at_gt: Optional[datetime]
    created_at_lt: Optional[datetime]
    include_archived: Optional[bool]
    limit: Optional[int]
    page: Optional[str]
    workspace_id: Optional[str]
    statuses: List[Literal["pending", "running", "completed", "failed", "canceled"]]
    betas: List[str]
