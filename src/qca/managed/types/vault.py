from __future__ import annotations

from datetime import datetime
from typing import Dict, Optional

from qca.common._models import BaseModel

__all__ = ["Vault"]


class Vault(BaseModel):
    id: Optional[str] = None
    archived_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    display_name: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None
    type: Optional[str] = None
    updated_at: Optional[datetime] = None
