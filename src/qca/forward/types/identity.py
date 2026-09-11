from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, Optional

from qca.common._models import BaseModel

__all__ = ["Identity"]


class Identity(BaseModel):
    id: Optional[str] = None
    external_id: Optional[str] = None
    name: Optional[str] = None
    identity_type: Optional[str] = None
    enabled: Optional[bool] = None
    metadata: Optional[Dict[str, Any]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
