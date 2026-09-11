from __future__ import annotations

from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["EnvironmentWorkListParams"]


class EnvironmentWorkListParams(TypedDict, total=False):
    before_id: Optional[str]
    after_id: Optional[str]
    page: Optional[str]
    limit: Optional[int]
    betas: List[str]
