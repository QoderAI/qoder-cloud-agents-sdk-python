from __future__ import annotations

from typing import Literal, Optional

from qca.common._models import BaseModel

__all__ = ["SessionWorkData"]


class SessionWorkData(BaseModel):
    id: Optional[str] = None
    type: Optional[Literal["session"]] = None
