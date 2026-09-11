from __future__ import annotations

from datetime import datetime
from typing import Optional

from qca.common._models import BaseModel

__all__ = ["FileResource"]


class FileResource(BaseModel):
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    file_id: Optional[str] = None
    mount_path: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[datetime] = None
