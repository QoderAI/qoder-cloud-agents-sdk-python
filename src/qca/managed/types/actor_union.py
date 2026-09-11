from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["ActorUnion"]


class ActorUnion(BaseModel):
    session_id: Optional[str] = None
    type: Optional[str] = None
    api_key_id: Optional[str] = None
    user_id: Optional[str] = None
    service_account_id: Optional[str] = None
