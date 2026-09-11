from __future__ import annotations

from typing import Literal, Optional

from typing_extensions import Required, TypedDict

__all__ = ["CustomSkillParams"]


class CustomSkillParams(TypedDict, total=False):
    skill_id: Required[str]
    type: Required[Literal["custom"]]
    version: Optional[str]
