from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["SkillVersionListParams"]


class SkillVersionListParams(TypedDict, total=False):
    identity_id: str
    """Select identity ownership with a PAT. Omit when using a SAT."""
    limit: Optional[int]
    page: Optional[str]
