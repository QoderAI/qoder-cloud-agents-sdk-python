from __future__ import annotations

from typing import Dict, List, Optional

from typing_extensions import Required, TypedDict

from qca.common._types import FileTypes

__all__ = ["FileUploadParams"]


class FileUploadParams(TypedDict, total=False):
    name: Optional[str]
    metadata: Dict[str, str]
    file: Required[FileTypes]
    expires_in_seconds: Optional[int]
    workspace_id: Optional[str]
    betas: List[str]
