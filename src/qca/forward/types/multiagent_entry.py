from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["MultiagentEntry"]


class MultiagentEntry(BaseModel):
    type: Optional[str] = None
    template_id: Optional[str] = None
    name: Optional[str] = None
