from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .batch_task_artifacts_item import BatchTaskArtifactsItem
    from .batch_task_error import BatchTaskError
    from .batch_task_usage import BatchTaskUsage

__all__ = ["BatchTask"]


class BatchTask(BaseModel):
    custom_id: Optional[str] = None
    status: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    output_summary: Optional[str] = None
    usage: Optional[BatchTaskUsage] = None
    artifacts: Optional[List[BatchTaskArtifactsItem]] = None
    error: Optional[BatchTaskError] = None
