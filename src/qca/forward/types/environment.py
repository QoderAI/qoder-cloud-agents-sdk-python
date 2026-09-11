from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .environment_config import EnvironmentConfig

__all__ = ["Environment"]


class Environment(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    config: Optional[EnvironmentConfig] = None
    metadata: Optional[Dict[str, Any]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    identity_id: Optional[str] = None
    archived_at: Optional[datetime] = None
