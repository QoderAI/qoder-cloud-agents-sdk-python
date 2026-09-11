from __future__ import annotations

from typing import Literal, Optional

from qca.common._models import BaseModel

__all__ = ["SelfHostedWorkHeartbeatResponse"]


class SelfHostedWorkHeartbeatResponse(BaseModel):
    last_heartbeat: Optional[str] = None
    lease_extended: Optional[bool] = None
    state: Optional[str] = None
    ttl_seconds: Optional[int] = None
    type: Optional[Literal["work_heartbeat"]] = None
