from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Dict, Literal, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .file_scope import FileScope

__all__ = ["FileMetadata"]


class FileMetadata(BaseModel):
    metadata: Optional[Dict[str, str]] = None
    status: Optional[str] = None
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    filename: Optional[str] = None
    mime_type: Optional[str] = None
    size_bytes: Optional[int] = None
    type: Optional[Literal["file"]] = None
    downloadable: Optional[bool] = None
    expires_at: Optional[datetime] = None
    scope: Optional[FileScope] = None
