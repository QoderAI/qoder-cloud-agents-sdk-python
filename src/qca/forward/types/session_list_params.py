from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["SessionListParams"]


class SessionListParams(TypedDict, total=False):
    identity_i_ds: List[str]
    template_id: Optional[str]
    source_type: Optional[str]
    created_at_gt: Optional[datetime]
    created_at_gte: Optional[datetime]
    created_at_lt: Optional[datetime]
    created_at_lte: Optional[datetime]
    updated_at_gt: Optional[datetime]
    updated_at_gte: Optional[datetime]
    updated_at_lt: Optional[datetime]
    updated_at_lte: Optional[datetime]
    limit: Optional[int]
    after_id: Optional[str]
    before_id: Optional[str]
    order: Optional[str]
    include_archived: Optional[bool]
