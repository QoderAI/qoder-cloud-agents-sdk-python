from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, Optional

from qca.common._models import BaseModel

__all__ = ["Skill"]


class Skill(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    display_title: Optional[str] = None
    description: Optional[str] = None
    source: Optional[str] = None
    latest_version: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    identity_id: Optional[str] = None
    icon_url: Optional[str] = None
    binding_info: Optional[Dict[str, int]] = None
