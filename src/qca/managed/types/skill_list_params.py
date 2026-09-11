from __future__ import annotations

from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["SkillListParams"]


class SkillListParams(TypedDict, total=False):
    display_name: Optional[str]
    name: Optional[str]
    before_id: Optional[str]
    after_id: Optional[str]
    page: Optional[str]
    source: Optional[str]
    limit: Optional[int]
    workspace_id: Optional[str]
    betas: List[str]
