from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["VaultCredentialAuth"]


class VaultCredentialAuth(BaseModel):
    type: Optional[str] = None
    mcp_server_url: Optional[str] = None
