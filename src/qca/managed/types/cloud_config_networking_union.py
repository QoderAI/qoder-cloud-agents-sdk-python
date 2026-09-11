from __future__ import annotations

from typing import List, Optional

from qca.common._models import BaseModel

__all__ = ["CloudConfigNetworkingUnion"]


class CloudConfigNetworkingUnion(BaseModel):
    type: Optional[str] = None
    allow_mcp_servers: Optional[bool] = None
    allow_package_managers: Optional[bool] = None
    allowed_hosts: Optional[List[str]] = None
