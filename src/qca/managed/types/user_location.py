from __future__ import annotations

from typing import Literal, Optional

from qca.common._models import BaseModel

__all__ = ["UserLocation"]


class UserLocation(BaseModel):
    type: Optional[Literal["approximate"]] = None
    city: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    timezone: Optional[str] = None
