from __future__ import annotations

from typing import Literal, Optional

from typing_extensions import Required, TypedDict

__all__ = ["FileResourceParams"]


class FileResourceParams(TypedDict, total=False):
    file_id: Required[str]
    type: Required[Literal["file"]]
    mount_path: Optional[str]
