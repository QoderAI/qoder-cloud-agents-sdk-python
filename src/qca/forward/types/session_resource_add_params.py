from __future__ import annotations

from typing import Optional

from typing_extensions import Required, TypedDict

__all__ = ["SessionResourceAddParams"]


class SessionResourceAddParams(TypedDict, total=False):
    type: Required[str]
    file_id: Required[str]
    mount_path: Optional[str]
