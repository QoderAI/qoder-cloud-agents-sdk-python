from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from qca.common._models import BaseModel


class DecisionChoice(BaseModel):
    value: str | bool
    description: str | None = None


class DecisionLevel(BaseModel):
    label: str
    score: float
    description: str | None = None


class DecisionQuestion(BaseModel):
    type: Literal["choice", "score"]
    instructions: str
    name: str | None = None
    choices: list[DecisionChoice] | None = None
    levels: list[DecisionLevel] | None = None


class DecisionAnswer(BaseModel):
    type: Literal["choice", "score", "refusal"]
    name: str | None = None
    value: str | bool | None = None
    score: float | None = None
    refusal: str | None = None


class DecisionContext(BaseModel):
    """Server-selected input metadata. Estimates are not billed model usage.

    Session-only fields and preparation metadata may be absent, especially on
    running or failed records. Unknown fields remain accessible as model extras.
    """

    mode: Literal["state", "session"]
    policy_version: str | None = None
    token_estimator: str | None = None
    estimated_input_tokens: int | None = None
    max_input_tokens: int | None = None
    snapshot_at: datetime | None = None
    anchor_event_id: str | None = None
    first_event_id: str | None = None
    last_event_id: str | None = None
    included_segment_count: int | None = None
    included_event_count: int | None = None
    scan_limited: bool | None = None
    truncated: bool | None = None
    truncation_reasons: list[str] | None = None


class DecisionError(BaseModel):
    code: str
    message: str


class Decision(BaseModel):
    """A stored evaluation. Retrieval and listing also expose running/failed records."""

    id: str
    session_id: str | None
    source: str
    status: Literal["running", "completed", "failed"]
    questions: list[DecisionQuestion]
    answers: list[DecisionAnswer]
    context: DecisionContext
    usage: dict[str, Any] | None
    error: DecisionError | None
    created_at: datetime
    completed_at: datetime | None
