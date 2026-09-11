from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, Optional

from qca.common._models import BaseModel

__all__ = ["FileMetadata"]


class FileMetadata(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    filename: Optional[str] = None
    size_bytes: Optional[int] = None
    mime_type: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    downloadable: Optional[bool] = None
    scope: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None
    identity_id: Optional[str] = None
