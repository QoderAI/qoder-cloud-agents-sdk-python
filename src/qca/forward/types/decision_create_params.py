from __future__ import annotations

from typing import Any, Literal, Union

from typing_extensions import Required, TypedDict


class DecisionChoiceParam(TypedDict, total=False):
    value: Required[Union[str, bool]]
    description: str


class DecisionLevelParam(TypedDict, total=False):
    label: Required[str]
    score: Required[float]
    description: str


class DecisionChoiceQuestionParam(TypedDict, total=False):
    type: Required[Literal["choice"]]
    instructions: Required[str]
    name: str
    choices: Required[list[DecisionChoiceParam]]


class DecisionScoreQuestionParam(TypedDict, total=False):
    type: Required[Literal["score"]]
    instructions: Required[str]
    name: str
    levels: Required[list[DecisionLevelParam]]


DecisionQuestionParam = Union[DecisionChoiceQuestionParam, DecisionScoreQuestionParam]


class DecisionCreateParams(TypedDict, total=False):
    """Provide exactly one of session_id and state, plus 1-32 questions.

    State must be a nonempty JSON object; state.session_context is reserved.
    Choice questions require 2-32 distinct string/boolean options; score
    questions require 2-32 finite numeric levels. No model parameter is accepted.
    """

    questions: Required[list[DecisionQuestionParam]]
    session_id: str
    state: dict[str, Any]
    idempotency_key: str
