from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, Optional

from qca.common._models import BaseModel

__all__ = ["SkillVersion"]


class SkillVersion(BaseModel):
    id: Optional[str] = None
    skill_id: Optional[str] = None
    version: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    directory: Optional[str] = None
    content_size: Optional[int] = None
    content_sha256: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    metadata: Optional[Dict[str, Any]] = None
