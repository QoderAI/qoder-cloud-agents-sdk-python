from __future__ import annotations

from typing import List, Literal

from typing_extensions import Required, TypedDict

__all__ = ["DreamSessionsInputParam"]


class DreamSessionsInputParam(TypedDict, total=False):
    session_ids: Required[List[str]]
    type: Required[Literal["sessions"]]
