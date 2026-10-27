from typing import Optional

from qca.common._models import BaseModel

__all__ = ["ModelConfig"]


class ModelConfig(BaseModel):
    inference_geo: Optional[str] = None
    id: Optional[str] = None
    effort: Optional[str] = None
    context_window: Optional[int] = None
    effective_context_window: Optional[int] = None
