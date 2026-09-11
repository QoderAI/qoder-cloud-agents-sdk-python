from __future__ import annotations

from typing import List, Optional

from qca.common._models import BaseModel

__all__ = ["Model"]


class Model(BaseModel):
    id: Optional[str] = None
    display_name: Optional[str] = None
    is_enabled: Optional[bool] = None
    is_new: Optional[bool] = None
    is_vl: Optional[bool] = None
    support_disable_reasoning: Optional[bool] = None
    price_factor: Optional[float] = None
    efforts: Optional[List[str]] = None
    default_effort: Optional[str] = None
    speed: Optional[List[str]] = None
    max_input_tokens: Optional[int] = None
    default_context_window: Optional[int] = None
    available_context_windows: Optional[List[int]] = None
