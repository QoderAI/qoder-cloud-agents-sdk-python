from __future__ import annotations

from typing import Literal, Optional

from typing_extensions import Required, TypedDict

__all__ = ["QoderSkillParams"]


class QoderSkillParams(TypedDict, total=False):
    skill_id: Required[str]
    type: Required[Literal["qoder"]]
    version: Optional[str]
