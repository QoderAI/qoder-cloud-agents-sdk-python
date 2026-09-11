from __future__ import annotations

from datetime import datetime
from typing import Optional

from qca.common._models import BaseModel

__all__ = ["SessionResource"]


class SessionResource(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    file_id: Optional[str] = None
    mount_path: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
