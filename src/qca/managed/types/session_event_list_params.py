from __future__ import annotations

from datetime import datetime
from typing import List, Literal, Optional

from typing_extensions import TypedDict

__all__ = ["SessionEventListParams"]


class SessionEventListParams(TypedDict, total=False):
    before_id: Optional[str]
    after_id: Optional[str]
    created_at_gt: Optional[datetime]
    created_at_gte: Optional[datetime]
    created_at_lt: Optional[datetime]
    created_at_lte: Optional[datetime]
    limit: Optional[int]
    page: Optional[str]
    workspace_id: Optional[str]
    order: Literal["asc", "desc"]
    types: List[str]
    betas: List[str]
