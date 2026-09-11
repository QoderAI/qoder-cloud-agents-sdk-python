from __future__ import annotations

from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["SkillVersionListParams"]


class SkillVersionListParams(TypedDict, total=False):
    limit: Optional[int]
    page: Optional[str]
    workspace_id: Optional[str]
    betas: List[str]
