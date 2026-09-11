from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .content_block_param import ContentBlockParam

__all__ = ["SessionEventParam"]


class SessionEventParam(TypedDict, total=False):
    type: Required[str]
    content: Union[List[ContentBlockParam], str, Dict[str, Any]]
    tool_use_id: Optional[str]
    custom_tool_use_id: Optional[str]
    result: Optional[str]
    deny_message: Optional[str]
    is_error: Optional[bool]
    description: Optional[str]
    rubric: Optional[str]
    outcome_id: Optional[str]
    max_iterations: Optional[int]
