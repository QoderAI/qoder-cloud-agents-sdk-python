from __future__ import annotations

from typing import List, Optional

from qca.common._models import BaseModel

__all__ = ["EnvironmentVariableAuthResponseNetworkingUnion"]


class EnvironmentVariableAuthResponseNetworkingUnion(BaseModel):
    type: Optional[str] = None
    allowed_hosts: Optional[List[str]] = None
