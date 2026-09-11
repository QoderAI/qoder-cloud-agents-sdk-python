from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .session_config import SessionConfig
    from .session_resource import SessionResource
    from .session_stats import SessionStats
    from .session_template import SessionTemplate
    from .session_usage import SessionUsage

__all__ = ["Session"]


class Session(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    identity_id: Optional[str] = None
    template: Optional[SessionTemplate] = None
    source_type: Optional[str] = None
    status: Optional[str] = None
    title: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    config: Optional[SessionConfig] = None
    resources: Optional[List[SessionResource]] = None
    stats: Optional[SessionStats] = None
    usage: Optional[SessionUsage] = None
    archived_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
