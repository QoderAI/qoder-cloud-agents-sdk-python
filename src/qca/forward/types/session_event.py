from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, Optional, Union

from qca.common._models import BaseModel

from .budget_limit import BudgetLimit
from .outcome_rubric import OutcomeRubric
from .tool_approval_evaluation import ToolApprovalEvaluation

__all__ = ["SessionEvent"]


class SessionEvent(BaseModel):
    evaluation: Optional[ToolApprovalEvaluation] = None
    budget: Optional[BudgetLimit] = None
    reason: Optional[str] = None
    iteration: Optional[int] = None
    explanation: Optional[str] = None
    outcome_evaluation_start_id: Optional[str] = None
    # Cumulative Credits: replace with the latest values, never sum successive events.
    model_credits: Optional[float] = None
    sandbox_runtime_credits: Optional[float] = None
    total_credits: Optional[float] = None
    id: Optional[str] = None
    type: Optional[str] = None
    session_id: Optional[str] = None
    content: Optional[Any] = None
    processed_at: Optional[datetime] = None
    session_thread_id: Optional[str] = None
    thinking: Optional[str] = None
    text: Optional[str] = None
    tool_use_id: Optional[str] = None
    custom_tool_use_id: Optional[str] = None
    mcp_tool_use_id: Optional[str] = None
    name: Optional[str] = None
    mcp_server_name: Optional[str] = None
    input: Optional[Dict[str, Any]] = None
    is_error: Optional[bool] = None
    result: Optional[str] = None
    deny_message: Optional[str] = None
    description: Optional[str] = None
    rubric: Optional[OutcomeRubric] = None
    outcome_id: Optional[str] = None
    max_iterations: Optional[int] = None
    message_id: Optional[str] = None
    message: Optional[Any] = None
    index: Optional[int] = None
    content_block: Optional[Any] = None
    delta: Optional[Any] = None
    event: Optional[Any] = None
    event_id: Optional[str] = None
    usage: Optional[Dict[str, Any]] = None
    stop_reason: Optional[Dict[str, Any]] = None
    error: Optional[Dict[str, Any]] = None
    evaluated_permission: Optional[Union[str, Dict[str, Any]]] = None
    file_id: Optional[str] = None
    original_filename: Optional[str] = None
    size: Optional[int] = None
    content_type: Optional[str] = None
    agent: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None
    title: Optional[str] = None
    model_request_start_id: Optional[str] = None
    model_usage: Optional[Dict[str, Any]] = None
