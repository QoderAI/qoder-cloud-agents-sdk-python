from __future__ import annotations

from typing import Literal, Optional

from typing_extensions import Required, TypedDict

__all__ = ["UserToolConfirmationEventParams"]


class UserToolConfirmationEventParams(TypedDict, total=False):
    result: Required[Literal["allow", "deny"]]
    tool_use_id: Required[str]
    type: Required[Literal["user.tool_confirmation"]]
    deny_message: Optional[str]
