from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .identity_config_spec import IdentityConfigSpec

__all__ = ["IdentityConfig"]


class IdentityConfig(BaseModel):
    type: Optional[str] = None
    id: Optional[str] = None
    identity_id: Optional[str] = None
    template_id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    effective_hash: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    identity_config: Optional[IdentityConfigSpec] = None
    metadata: Optional[Dict[str, Any]] = None
