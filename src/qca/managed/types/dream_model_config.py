from typing import Optional

from qca.common._models import BaseModel

__all__ = ["DreamModelConfig"]


class DreamModelConfig(BaseModel):
    id: Optional[str] = None
    effort: Optional[str] = None
    context_window: Optional[int] = None
