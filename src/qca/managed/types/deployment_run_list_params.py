from __future__ import annotations

from datetime import datetime
from typing import List, Literal, Optional

from typing_extensions import TypedDict

__all__ = ["DeploymentRunListParams"]


class DeploymentRunListParams(TypedDict, total=False):
    before_id: Optional[str]
    after_id: Optional[str]
    created_at_gt: Optional[datetime]
    created_at_gte: Optional[datetime]
    created_at_lt: Optional[datetime]
    created_at_lte: Optional[datetime]
    deployment_id: Optional[str]
    has_error: Optional[bool]
    limit: Optional[int]
    page: Optional[str]
    workspace_id: Optional[str]
    trigger_type: Literal["schedule", "manual"]
    betas: List[str]
