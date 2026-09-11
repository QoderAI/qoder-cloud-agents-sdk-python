from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, Optional

from qca.common._models import BaseModel

__all__ = ["Vault"]


class Vault(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    display_name: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    identity_id: Optional[str] = None
