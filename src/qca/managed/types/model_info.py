from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Literal, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .model_capabilities import ModelCapabilities

__all__ = ["ModelInfo"]


class ModelInfo(BaseModel):
    source: Optional[str] = None
    is_enabled: Optional[bool] = None
    is_new: Optional[bool] = None
    price_factor: Optional[float] = None
    efforts: Optional[List[str]] = None
    default_effort: Optional[str] = None
    default_context_window: Optional[int] = None
    available_context_windows: Optional[List[int]] = None
    id: Optional[str] = None
    allowed_fallback_models: Optional[List[str]] = None
    capabilities: Optional[ModelCapabilities] = None
    created_at: Optional[datetime] = None
    display_name: Optional[str] = None
    max_input_tokens: Optional[int] = None
    max_tokens: Optional[int] = None
    type: Optional[Literal["model"]] = None
