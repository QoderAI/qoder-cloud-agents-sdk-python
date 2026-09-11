from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .cache_creation_usage import CacheCreationUsage
    from .monetary_amount import MonetaryAmount
    from .server_tool_usage import ServerToolUsage

__all__ = ["SessionUsage"]


class SessionUsage(BaseModel):
    active_seconds: Optional[float] = None
    cache_creation: Optional[CacheCreationUsage] = None
    cache_read_input_tokens: Optional[int] = None
    input_tokens: Optional[int] = None
    list_cost: Optional[MonetaryAmount] = None
    output_tokens: Optional[int] = None
    server_tool_use: Optional[ServerToolUsage] = None
