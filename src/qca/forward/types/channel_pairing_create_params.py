from __future__ import annotations

from typing import Optional

from typing_extensions import Required, TypedDict

__all__ = ["ChannelPairingCreateParams"]


class ChannelPairingCreateParams(TypedDict, total=False):
    code: str
    """Supply exactly one of code or channel_pairing_id."""
    channel_pairing_id: str
    identity_id: Required[str]
    template_id: Required[str]
    idempotency_key: Optional[str]
