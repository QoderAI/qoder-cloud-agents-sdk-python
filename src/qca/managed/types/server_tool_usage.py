from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["ServerToolUsage"]


class ServerToolUsage(BaseModel):
    web_fetch_requests: Optional[int] = None
    web_search_requests: Optional[int] = None
