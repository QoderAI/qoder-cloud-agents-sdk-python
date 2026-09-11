from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["BatchTaskArtifactsItem"]


class BatchTaskArtifactsItem(BaseModel):
    file_id: Optional[str] = None
    name: Optional[str] = None
    size: Optional[int] = None
    content_type: Optional[str] = None
