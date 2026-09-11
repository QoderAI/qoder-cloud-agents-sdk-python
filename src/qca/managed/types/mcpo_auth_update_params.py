from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Literal, Optional

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .mcpo_auth_refresh_update_params import MCPOAuthRefreshUpdateParams

__all__ = ["MCPOAuthUpdateParams"]


class MCPOAuthUpdateParams(TypedDict, total=False):
    type: Required[Literal["mcp_oauth"]]
    access_token: Optional[str]
    expires_at: Optional[datetime]
    refresh: MCPOAuthRefreshUpdateParams
