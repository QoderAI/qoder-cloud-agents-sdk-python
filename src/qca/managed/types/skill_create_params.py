from __future__ import annotations

from typing import Dict, List, Optional

from typing_extensions import Required, TypedDict

from qca.common._types import FileTypes

__all__ = ["SkillCreateParams"]


class SkillCreateParams(TypedDict, total=False):
    metadata: Dict[str, str]
    files: Required[List[FileTypes]]
    display_title: Optional[str]
    workspace_id: Optional[str]
    betas: List[str]
