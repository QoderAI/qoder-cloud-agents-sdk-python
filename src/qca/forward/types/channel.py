from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .channel_channel_config import ChannelChannelConfig
    from .channel_identity_resolution import ChannelIdentityResolution

__all__ = ["Channel"]


class Channel(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    identity_id: Optional[str] = None
    identity_resolution: Optional[ChannelIdentityResolution] = None
    template_id: Optional[str] = None
    channel_type: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[bool] = None
    binding_status: Optional[str] = None
    channel_config: Optional[ChannelChannelConfig] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
