from __future__ import annotations

from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["EnvironmentWorkHeartbeatParams"]


class EnvironmentWorkHeartbeatParams(TypedDict, total=False):
    desired_ttl_seconds: Optional[int]
    expected_last_heartbeat: Optional[str]
    betas: List[str]
