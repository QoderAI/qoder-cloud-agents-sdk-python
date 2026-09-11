from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["SearchResultContent"]


class SearchResultContent(BaseModel):
    text: Optional[str] = None
    type: Optional[str] = None
