from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .image_source_param import ImageSourceParam

__all__ = ["ContentBlockParam"]


class ContentBlockParam(TypedDict, total=False):
    type: Required[str]
    text: Optional[str]
    thinking: Optional[str]
    source: ImageSourceParam
