from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Optional, Union

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .system_content_block import SystemContentBlock
    from .user_custom_tool_result_event_content_union import UserCustomToolResultEventContentUnion
    from .user_define_outcome_event_rubric_union import UserDefineOutcomeEventRubricUnion
    from .user_message_event_content_union import UserMessageEventContentUnion
    from .user_tool_result_event_content_union import UserToolResultEventContentUnion

__all__ = ["SendSessionEventsDataUnion"]


class SendSessionEventsDataUnion(BaseModel):
    id: Optional[str] = None
    content: Optional[
        Union[
            List[UserMessageEventContentUnion],
            List[UserCustomToolResultEventContentUnion],
            List[UserToolResultEventContentUnion],
            List[SystemContentBlock],
        ]
    ] = None
    type: Optional[str] = None
    processed_at: Optional[datetime] = None
    session_thread_id: Optional[str] = None
    result: Optional[str] = None
    tool_use_id: Optional[str] = None
    deny_message: Optional[str] = None
    custom_tool_use_id: Optional[str] = None
    is_error: Optional[bool] = None
    description: Optional[str] = None
    max_iterations: Optional[int] = None
    outcome_id: Optional[str] = None
    rubric: Optional[UserDefineOutcomeEventRubricUnion] = None
