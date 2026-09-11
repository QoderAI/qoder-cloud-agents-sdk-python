from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["SkillRetrieveParams"]


class SkillRetrieveParams(TypedDict, total=False):
    include_content: Optional[bool]
