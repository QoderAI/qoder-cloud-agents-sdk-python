from __future__ import annotations

from typing import Any, Dict, Optional

from typing_extensions import Required, TypedDict

from qca.common._types import FileTypes

__all__ = ["FileUploadParams"]


class FileUploadParams(TypedDict, total=False):
    identity_id: str
    """Select identity ownership with a PAT. Omit when using a SAT."""
    file: Required[FileTypes]
    name: Optional[str]
    purpose: Optional[str]
    metadata: Dict[str, Any]
    idempotency_key: Optional[str]
