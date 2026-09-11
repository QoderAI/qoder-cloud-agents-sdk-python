from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["ChannelPairing"]


class ChannelPairing(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    channel_id: Optional[str] = None
    identity_id: Optional[str] = None
    template_id: Optional[str] = None
    status: Optional[str] = None
    paired_at: Optional[str] = None
