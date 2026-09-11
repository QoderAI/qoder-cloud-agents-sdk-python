from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["FileDocumentSourceParam"]


class FileDocumentSourceParam(TypedDict, total=False):
    file_id: Required[str]
    type: Required[Literal["file"]]
