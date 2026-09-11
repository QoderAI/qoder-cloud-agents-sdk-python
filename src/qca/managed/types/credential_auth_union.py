from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .environment_variable_auth_response_networking_union import EnvironmentVariableAuthResponseNetworkingUnion
    from .injection_location_response import InjectionLocationResponse
    from .mcpo_auth_refresh_response import MCPOAuthRefreshResponse

__all__ = ["CredentialAuthUnion"]


class CredentialAuthUnion(BaseModel):
    mcp_server_url: Optional[str] = None
    type: Optional[str] = None
    expires_at: Optional[datetime] = None
    refresh: Optional[MCPOAuthRefreshResponse] = None
    injection_location: Optional[InjectionLocationResponse] = None
    networking: Optional[EnvironmentVariableAuthResponseNetworkingUnion] = None
    secret_name: Optional[str] = None
