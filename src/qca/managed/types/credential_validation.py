from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .mcp_probe import MCPProbe
    from .refresh_object import RefreshObject

__all__ = ["CredentialValidation"]


class CredentialValidation(BaseModel):
    credential_id: Optional[str] = None
    has_refresh_token: Optional[bool] = None
    mcp_probe: Optional[MCPProbe] = None
    refresh: Optional[RefreshObject] = None
    status: Optional[str] = None
    type: Optional[str] = None
    validated_at: Optional[datetime] = None
    vault_id: Optional[str] = None
