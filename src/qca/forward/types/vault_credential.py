from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .vault_credential_auth import VaultCredentialAuth

__all__ = ["VaultCredential"]


class VaultCredential(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    vault_id: Optional[str] = None
    auth: Optional[VaultCredentialAuth] = None
    display_name: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
