from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .batch_request_counts import BatchRequestCounts
    from .batch_usage import BatchUsage

__all__ = ["Batch"]


class Batch(BaseModel):
    id: Optional[str] = None
    object: Optional[str] = None
    status: Optional[str] = None
    input_file_id: Optional[str] = None
    output_file_id: Optional[str] = None
    completion_window: Optional[str] = None
    created_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    request_counts: Optional[BatchRequestCounts] = None
    usage: Optional[BatchUsage] = None
    metadata: Optional[Dict[str, Any]] = None
    total: Optional[int] = None
    pending: Optional[int] = None
    running: Optional[int] = None
    completed: Optional[int] = None
    failed: Optional[int] = None
    cancelled: Optional[int] = None
    expired: Optional[int] = None
    error_file_id: Optional[str] = None
    error_message: Optional[str] = None
