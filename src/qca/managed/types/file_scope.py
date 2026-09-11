from __future__ import annotations

from typing import Literal, Optional

from qca.common._models import BaseModel

__all__ = ["FileScope"]


class FileScope(BaseModel):
    id: Optional[str] = None
    type: Optional[Literal["session"]] = None
