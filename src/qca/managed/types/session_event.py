from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .agent_mcp_tool_result_event_content_union import AgentMCPToolResultEventContentUnion
    from .agent_message_event_content_union import AgentMessageEventContentUnion
    from .agent_thread_message_received_event_content_union import AgentThreadMessageReceivedEventContentUnion
    from .agent_thread_message_sent_event_content_union import AgentThreadMessageSentEventContentUnion
    from .agent_tool_result_event_content_union import AgentToolResultEventContentUnion
    from .budget_limit import BudgetLimit
    from .session_agent import SessionAgent
    from .session_error_event_error_union import SessionErrorEventErrorUnion
    from .session_event_stop_reason import SessionEventStopReason
    from .session_event_usage import SessionEventUsage
    from .span_model_usage import SpanModelUsage
    from .system_content_block import SystemContentBlock
    from .user_custom_tool_result_event_content_union import UserCustomToolResultEventContentUnion
    from .user_define_outcome_event_rubric_union import UserDefineOutcomeEventRubricUnion
    from .user_message_event_content_union import UserMessageEventContentUnion
    from .user_tool_result_event_content_union import UserToolResultEventContentUnion

__all__ = ["SessionEvent"]


class SessionEvent(BaseModel):
    id: Optional[str] = None
    content: Optional[
        Union[
            List[UserMessageEventContentUnion],
            List[UserCustomToolResultEventContentUnion],
            List[AgentMessageEventContentUnion],
            List[AgentMCPToolResultEventContentUnion],
            List[AgentToolResultEventContentUnion],
            List[AgentThreadMessageReceivedEventContentUnion],
            List[AgentThreadMessageSentEventContentUnion],
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
    input: Optional[Any] = None
    name: Optional[str] = None
    mcp_server_name: Optional[str] = None
    evaluated_permission: Optional[str] = None
    mcp_tool_use_id: Optional[str] = None
    from_session_thread_id: Optional[str] = None
    from_agent_name: Optional[str] = None
    to_session_thread_id: Optional[str] = None
    to_agent_name: Optional[str] = None
    error: Optional[SessionErrorEventErrorUnion] = None
    stop_reason: Optional[SessionEventStopReason] = None
    agent_name: Optional[str] = None
    iteration: Optional[int] = None
    outcome_id: Optional[str] = None
    explanation: Optional[str] = None
    outcome_evaluation_start_id: Optional[str] = None
    usage: Optional[SessionEventUsage] = None
    model_request_start_id: Optional[str] = None
    model_usage: Optional[SpanModelUsage] = None
    description: Optional[str] = None
    max_iterations: Optional[int] = None
    rubric: Optional[UserDefineOutcomeEventRubricUnion] = None
    agent: Optional[SessionAgent] = None
    budget: Optional[BudgetLimit] = None
    metadata: Optional[Dict[str, str]] = None
    title: Optional[str] = None
