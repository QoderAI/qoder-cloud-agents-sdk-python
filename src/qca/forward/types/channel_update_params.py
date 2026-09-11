from __future__ import annotations

from typing import Any, Dict, Optional

from typing_extensions import TypedDict

__all__ = ["ChannelUpdateParams"]


class ChannelUpdateParams(TypedDict, total=False):
    name: Optional[str]
    identity_id: Optional[str]
    template_id: Optional[str]
    enabled: Optional[bool]
    channel_config: Dict[str, Any]
    idempotency_key: Optional[str]
