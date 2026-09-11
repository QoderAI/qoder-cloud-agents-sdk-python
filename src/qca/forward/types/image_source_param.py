from __future__ import annotations

from typing import Optional

from typing_extensions import Required, TypedDict

__all__ = ["ImageSourceParam"]


class ImageSourceParam(TypedDict, total=False):
    type: Required[str]
    media_type: Optional[str]
    data: Optional[str]
    url: Optional[str]
    file_id: Optional[str]
