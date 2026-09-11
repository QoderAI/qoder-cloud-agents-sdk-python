from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["ChannelQRSession"]


class ChannelQRSession(BaseModel):
    session_key: Optional[str] = None
    channel_id: Optional[str] = None
    channel_type: Optional[str] = None
    status: Optional[str] = None
    qr_code_content: Optional[str] = None
    qr_code_image_base64: Optional[str] = None
    expires_at: Optional[str] = None
    err_code: Optional[str] = None
    err_msg: Optional[str] = None
