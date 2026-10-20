from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["SkillListParams"]


class SkillListParams(TypedDict, total=False):
    identity_id: str
    """Select identity ownership with a PAT. Omit when using a SAT."""
    limit: Optional[int]
    page: Optional[str]
    after_id: Optional[str]
    before_id: Optional[str]
    display_title: Optional[str]
    source: Optional[str]
    name: Optional[str]
