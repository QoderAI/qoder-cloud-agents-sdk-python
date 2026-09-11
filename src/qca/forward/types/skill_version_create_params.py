from __future__ import annotations

from typing import List

from typing_extensions import Required, TypedDict

from qca.common._types import FileTypes

__all__ = ["SkillVersionCreateParams"]


class SkillVersionCreateParams(TypedDict, total=False):
    files: Required[List[FileTypes]]
