from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .model_config_effort_union import ModelConfigEffortUnion

__all__ = ["ModelConfig"]


class ModelConfig(BaseModel):
    context_window: Optional[int] = None
    id: Optional[str] = None
    effort: Optional[ModelConfigEffortUnion] = None
    inference_geo: Optional[str] = None
    speed: Optional[str] = None
