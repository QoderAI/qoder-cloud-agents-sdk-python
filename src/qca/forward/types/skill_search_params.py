from __future__ import annotations

from typing import Dict, Literal

from typing_extensions import TypedDict

__all__ = ["SkillSearchParams"]


class SkillSearchParams(TypedDict, total=False):
    metadata: Dict[str, str]
    limit: int
    page: str
    source: Literal["custom", "qoder"]
    display_title: str
    identity_id: str
