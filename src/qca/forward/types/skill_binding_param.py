from __future__ import annotations

from typing import Optional

from typing_extensions import Required, TypedDict

__all__ = ["SkillBindingParam"]


class SkillBindingParam(TypedDict, total=False):
    type: Required[str]
    skill_id: Required[str]
    version: Optional[str]
    enabled: Optional[bool]
