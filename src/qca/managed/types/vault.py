from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Dict, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .credential import Credential

__all__ = ["Vault"]


class Vault(BaseModel):
    # Empty on creation. Use the separate Credential API to add credentials.
    credentials: Optional[List[Credential]] = None
    id: Optional[str] = None
    archived_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    display_name: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None
    type: Optional[str] = None
    updated_at: Optional[datetime] = None
