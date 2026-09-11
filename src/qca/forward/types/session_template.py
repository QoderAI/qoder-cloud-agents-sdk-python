from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Union

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .model_config import ModelConfig

__all__ = ["SessionTemplate"]


class SessionTemplate(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None
    model: Optional[Union[str, ModelConfig]] = None
    version: Optional[int] = None
