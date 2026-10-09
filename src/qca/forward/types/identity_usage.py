from typing import Literal

from qca.common._models import BaseModel


class IdentityUsage(BaseModel):
    type: Literal["identity_usage"]
    identity_id: str
    session_count: int
    active_seconds: float
    credits: float
