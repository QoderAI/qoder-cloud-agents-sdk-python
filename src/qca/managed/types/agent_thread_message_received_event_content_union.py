from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .agent_thread_message_received_event_content_union_source import (
        AgentThreadMessageReceivedEventContentUnionSource,
    )

__all__ = ["AgentThreadMessageReceivedEventContentUnion"]


class AgentThreadMessageReceivedEventContentUnion(BaseModel):
    text: Optional[str] = None
    type: Optional[str] = None
    source: Optional[AgentThreadMessageReceivedEventContentUnionSource] = None
    context: Optional[str] = None
    title: Optional[str] = None
