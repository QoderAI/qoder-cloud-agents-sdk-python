from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .channel_channel_config_response_options import ChannelChannelConfigResponseOptions

__all__ = ["ChannelChannelConfig"]


class ChannelChannelConfig(BaseModel):
    response_options: Optional[ChannelChannelConfigResponseOptions] = None
