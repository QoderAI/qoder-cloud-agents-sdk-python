from __future__ import annotations

from datetime import datetime
from typing import Optional

from qca.common._models import BaseModel

__all__ = ["IdentityTemplate"]


class IdentityTemplate(BaseModel):
    template_id: Optional[str] = None
    template_name: Optional[str] = None
    session_count: Optional[int] = None
    last_active_at: Optional[datetime] = None
