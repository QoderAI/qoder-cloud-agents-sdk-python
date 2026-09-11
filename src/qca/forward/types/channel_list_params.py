from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["ChannelListParams"]


class ChannelListParams(TypedDict, total=False):
    channel_type: Optional[str]
    enabled: Optional[bool]
    binding_status: Optional[str]
    identity_id: Optional[str]
    template_id: Optional[str]
    limit: Optional[int]
    after_id: Optional[str]
    before_id: Optional[str]
