from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["UserMessageEventContentUnionSource"]


class UserMessageEventContentUnionSource(BaseModel):
    data: Optional[str] = None
    media_type: Optional[str] = None
    type: Optional[str] = None
    url: Optional[str] = None
    file_id: Optional[str] = None
