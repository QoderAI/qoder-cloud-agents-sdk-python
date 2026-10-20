from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["EnvironmentBindingInfo"]


class EnvironmentBindingInfo(BaseModel):
    agent_template_count: Optional[int] = None
