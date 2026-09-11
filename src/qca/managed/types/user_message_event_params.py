from __future__ import annotations

from typing import TYPE_CHECKING, List, Literal, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .document_block_param import DocumentBlockParam
    from .image_block_param import ImageBlockParam
    from .redacted_block_param import RedactedBlockParam
    from .text_block_param import TextBlockParam

__all__ = ["UserMessageEventParams"]


class UserMessageEventParams(TypedDict, total=False):
    content: Required[List[Union[TextBlockParam, ImageBlockParam, DocumentBlockParam, RedactedBlockParam]]]
    type: Required[Literal["user.message"]]
