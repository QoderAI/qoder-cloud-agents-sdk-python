from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["RefreshHTTPResponse"]


class RefreshHTTPResponse(BaseModel):
    body: Optional[str] = None
    body_truncated: Optional[bool] = None
    content_type: Optional[str] = None
    status_code: Optional[int] = None
