from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["ModelConfig"]


class ModelConfig(BaseModel):
    id: Optional[str] = None
    effort: Optional[str] = None
    context_window: Optional[int] = None
