from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .text_block import TextBlock

__all__ = ["DeltaContent"]


class DeltaContent(BaseModel):
    content: Optional[TextBlock] = None
    type: Optional[str] = None
    index: Optional[int] = None
