from __future__ import annotations

from typing import Any, Dict, Optional

from typing_extensions import TypedDict

__all__ = ["SkillUpdateParams"]


class SkillUpdateParams(TypedDict, total=False):
    description: Optional[str]
    content: Optional[str]
    content_encoding: Optional[str]
    metadata: Dict[str, Any]
    icon_id: Optional[str]
    name: Optional[str]
