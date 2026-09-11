from __future__ import annotations

from typing import Any, Dict, List, Optional

from typing_extensions import TypedDict

from qca.common._types import FileTypes

__all__ = ["SkillCreateParams"]


class SkillCreateParams(TypedDict, total=False):
    files: List[FileTypes]
    metadata: Dict[str, Any]
    icon_id: Optional[str]
    file: FileTypes
    name: Optional[str]
    description: Optional[str]
    type: Optional[str]
    idempotency_key: Optional[str]
