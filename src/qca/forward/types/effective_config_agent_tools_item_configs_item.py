from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["EffectiveConfigAgentToolsItemConfigsItem"]


class EffectiveConfigAgentToolsItemConfigsItem(BaseModel):
    name: Optional[str] = None
    enabled: Optional[bool] = None
