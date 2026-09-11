from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .agent_thread_message_sent_event_content_union_source import AgentThreadMessageSentEventContentUnionSource

__all__ = ["AgentThreadMessageSentEventContentUnion"]


class AgentThreadMessageSentEventContentUnion(BaseModel):
    text: Optional[str] = None
    type: Optional[str] = None
    source: Optional[AgentThreadMessageSentEventContentUnionSource] = None
    context: Optional[str] = None
    title: Optional[str] = None
