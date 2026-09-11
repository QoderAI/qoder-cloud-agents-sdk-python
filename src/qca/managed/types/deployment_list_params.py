from __future__ import annotations

from datetime import datetime
from typing import List, Literal, Optional

from typing_extensions import TypedDict

__all__ = ["DeploymentListParams"]


class DeploymentListParams(TypedDict, total=False):
    before_id: Optional[str]
    after_id: Optional[str]
    agent_id: Optional[str]
    created_at_gte: Optional[datetime]
    created_at_lte: Optional[datetime]
    include_archived: Optional[bool]
    limit: Optional[int]
    page: Optional[str]
    workspace_id: Optional[str]
    status: Literal["active", "paused"]
    betas: List[str]
