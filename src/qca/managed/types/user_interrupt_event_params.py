from __future__ import annotations

from typing import Literal, Optional

from typing_extensions import Required, TypedDict

__all__ = ["UserInterruptEventParams"]


class UserInterruptEventParams(TypedDict, total=False):
    type: Required[Literal["user.interrupt"]]
    session_thread_id: Optional[str]
