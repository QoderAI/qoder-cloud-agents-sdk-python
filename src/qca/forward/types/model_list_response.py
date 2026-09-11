from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .model import Model

__all__ = ["ModelListResponse"]


class ModelListResponse(BaseModel):
    data: Optional[List[Model]] = None
    has_more: Optional[bool] = None
