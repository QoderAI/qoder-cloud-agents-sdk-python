from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["SkillOverrideParam"]


class SkillOverrideParam(TypedDict, total=False):
    enabled: Optional[bool]
    type: Optional[str]
    version: Optional[str]
