from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["EffectiveConfigSessionResourcesItem"]


class EffectiveConfigSessionResourcesItem(BaseModel):
    type: Optional[str] = None
    file_id: Optional[str] = None
    url: Optional[str] = None
    mount_path: Optional[str] = None
