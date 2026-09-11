from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Dict, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .credential_auth_union import CredentialAuthUnion

__all__ = ["Credential"]


class Credential(BaseModel):
    id: Optional[str] = None
    archived_at: Optional[datetime] = None
    auth: Optional[CredentialAuthUnion] = None
    created_at: Optional[datetime] = None
    metadata: Optional[Dict[str, str]] = None
    type: Optional[str] = None
    updated_at: Optional[datetime] = None
    vault_id: Optional[str] = None
    display_name: Optional[str] = None
