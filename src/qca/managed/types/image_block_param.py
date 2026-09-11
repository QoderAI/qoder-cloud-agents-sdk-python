from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .base64_image_source_param import Base64ImageSourceParam
    from .file_image_source_param import FileImageSourceParam
    from .url_image_source_param import URLImageSourceParam

__all__ = ["ImageBlockParam"]


class ImageBlockParam(TypedDict, total=False):
    source: Required[Union[Base64ImageSourceParam, URLImageSourceParam, FileImageSourceParam]]
    type: Required[Literal["image"]]
