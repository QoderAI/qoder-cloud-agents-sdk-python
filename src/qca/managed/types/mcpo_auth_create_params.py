from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Literal, Optional

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .mcpo_auth_refresh_params import MCPOAuthRefreshParams

__all__ = ["MCPOAuthCreateParams"]


class MCPOAuthCreateParams(TypedDict, total=False):
    access_token: Required[str]
    mcp_server_url: Required[str]
    type: Required[Literal["mcp_oauth"]]
    expires_at: Optional[datetime]
    refresh: MCPOAuthRefreshParams
