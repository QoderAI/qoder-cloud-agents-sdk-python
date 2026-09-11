from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["IdentityClearResponseSummary"]


class IdentityClearResponseSummary(BaseModel):
    identity_configs_archived: Optional[int] = None
    resource_bindings_archived: Optional[int] = None
    identity_owned_resources_archived: Optional[int] = None
    schedules_archived: Optional[int] = None
    schedule_runs_skipped: Optional[int] = None
    sessions_archived: Optional[int] = None
