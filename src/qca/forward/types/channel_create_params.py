from __future__ import annotations

from typing import Any, Dict, Optional

from typing_extensions import Required, TypedDict

__all__ = ["ChannelCreateParams"]


class ChannelCreateParams(TypedDict, total=False):
    identity_id: Optional[str]
    identity_resolution: Dict[str, Any]
    template_id: Optional[str]
    channel_type: Required[str]
    name: Optional[str]
    enabled: Optional[bool]
    channel_config: Dict[str, Any]
    idempotency_key: Optional[str]
