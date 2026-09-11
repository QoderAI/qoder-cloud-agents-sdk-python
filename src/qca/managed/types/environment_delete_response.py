from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["EnvironmentDeleteResponse"]


class EnvironmentDeleteResponse(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
