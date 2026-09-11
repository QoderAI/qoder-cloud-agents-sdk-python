from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .cache_creation_usage import CacheCreationUsage
    from .monetary_amount import MonetaryAmount
    from .server_tool_usage import ServerToolUsage

__all__ = ["StreamSessionThreadEventsUnionUsage"]


class StreamSessionThreadEventsUnionUsage(BaseModel):
    cache_creation_input_tokens: Optional[int] = None
    cache_read_input_tokens: Optional[int] = None
    input_tokens: Optional[int] = None
    output_tokens: Optional[int] = None
    speed: Optional[str] = None
    active_seconds: Optional[float] = None
    cache_creation: Optional[CacheCreationUsage] = None
    list_cost: Optional[MonetaryAmount] = None
    server_tool_use: Optional[ServerToolUsage] = None
