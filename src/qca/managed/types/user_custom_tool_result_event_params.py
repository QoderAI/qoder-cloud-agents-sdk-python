from __future__ import annotations

from typing import TYPE_CHECKING, List, Literal, Optional, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .document_block_param import DocumentBlockParam
    from .image_block_param import ImageBlockParam
    from .search_result_block_param import SearchResultBlockParam
    from .text_block_param import TextBlockParam

__all__ = ["UserCustomToolResultEventParams"]


class UserCustomToolResultEventParams(TypedDict, total=False):
    custom_tool_use_id: Required[str]
    type: Required[Literal["user.custom_tool_result"]]
    is_error: Optional[bool]
    content: List[Union[TextBlockParam, ImageBlockParam, DocumentBlockParam, SearchResultBlockParam]]
