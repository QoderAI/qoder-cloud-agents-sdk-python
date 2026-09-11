from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["ChannelChannelConfigResponseOptions"]


class ChannelChannelConfigResponseOptions(BaseModel):
    include_tool_calls: Optional[bool] = None
    include_thinking: Optional[bool] = None
