from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["DreamUsage"]


class DreamUsage(BaseModel):
    cache_creation_input_tokens: Optional[int] = None
    cache_read_input_tokens: Optional[int] = None
    input_tokens: Optional[int] = None
    output_tokens: Optional[int] = None
