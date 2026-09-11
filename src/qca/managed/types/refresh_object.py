from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .refresh_http_response import RefreshHTTPResponse

__all__ = ["RefreshObject"]


class RefreshObject(BaseModel):
    http_response: Optional[RefreshHTTPResponse] = None
    status: Optional[str] = None
