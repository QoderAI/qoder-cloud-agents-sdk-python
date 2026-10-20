from __future__ import annotations

from typing import List

from typing_extensions import Required, TypedDict

from qca.common._types import FileTypes

__all__ = ["SkillVersionCreateParams"]


class SkillVersionCreateParams(TypedDict, total=False):
    identity_id: str
    """Select identity ownership with a PAT. Omit when using a SAT."""
    files: Required[List[FileTypes]]
