from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .user_message_event_content_union_source import UserMessageEventContentUnionSource

__all__ = ["UserMessageEventContentUnion"]


class UserMessageEventContentUnion(BaseModel):
    text: Optional[str] = None
    type: Optional[str] = None
    source: Optional[UserMessageEventContentUnionSource] = None
    context: Optional[str] = None
    title: Optional[str] = None
