from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["CacheCreationUsage"]


class CacheCreationUsage(BaseModel):
    ephemeral_1h_input_tokens: Optional[int] = None
    ephemeral_5m_input_tokens: Optional[int] = None
