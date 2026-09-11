from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["ScheduleArchiveManyResponse"]


class ScheduleArchiveManyResponse(BaseModel):
    archived_count: Optional[int] = None
