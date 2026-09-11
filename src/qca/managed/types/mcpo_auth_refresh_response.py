from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .mcpo_auth_refresh_response_token_endpoint_auth_union import MCPOAuthRefreshResponseTokenEndpointAuthUnion

__all__ = ["MCPOAuthRefreshResponse"]


class MCPOAuthRefreshResponse(BaseModel):
    client_id: Optional[str] = None
    token_endpoint: Optional[str] = None
    token_endpoint_auth: Optional[MCPOAuthRefreshResponseTokenEndpointAuthUnion] = None
    resource: Optional[str] = None
    scope: Optional[str] = None
