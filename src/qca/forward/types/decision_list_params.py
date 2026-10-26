from __future__ import annotations

from typing_extensions import TypedDict


class DecisionListParams(TypedDict, total=False):
    session_id: str
    limit: int
    after_id: str
    before_id: str
