from __future__ import annotations

from typing import List, Literal, Optional

from typing_extensions import TypedDict

__all__ = ["LimitedNetworkParams"]


class LimitedNetworkParams(TypedDict, total=False):
    allow_mcp_servers: Optional[bool]
    allow_package_managers: Optional[bool]
    allowed_hosts: List[str]
    type: Literal["limited"]
