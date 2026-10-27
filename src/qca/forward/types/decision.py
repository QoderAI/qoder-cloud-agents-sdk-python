from __future__ import annotations

from datetime import datetime
from typing import Literal

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
    type: Literal["choice", "score"]
    name: str | None = None
    value: str | bool | None = None
    score: float | None = None


class DecisionContext(BaseModel):
    """Input mode and the Session events used for evaluation.

    Session-only fields may be absent, especially on
    running or failed records. Unknown fields remain accessible as model extras.
    """

    mode: Literal["state", "session"]
    anchor_event_id: str | None = None
    first_event_id: str | None = None
    last_event_id: str | None = None
    included_segment_count: int | None = None
    included_event_count: int | None = None


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
    error: DecisionError | None
    created_at: datetime
    completed_at: datetime | None
