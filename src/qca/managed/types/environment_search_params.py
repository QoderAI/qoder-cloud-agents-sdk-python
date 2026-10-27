from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Union

from typing_extensions import TypedDict

__all__ = ["EnvironmentSearchParams"]


class EnvironmentSearchParams(TypedDict, total=False):
    metadata: Dict[str, str]
    limit: int
    page: str
    name: str
    include_archived: bool
    created_at_gte: Union[datetime, str]
    created_at_lte: Union[datetime, str]
    workspace_id: str
    betas: List[str]
