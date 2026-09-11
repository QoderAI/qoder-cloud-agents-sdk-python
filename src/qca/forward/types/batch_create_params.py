from __future__ import annotations

from typing import Any, Dict, Optional

from typing_extensions import Required, TypedDict

__all__ = ["BatchCreateParams"]


class BatchCreateParams(TypedDict, total=False):
    input_file_id: Required[str]
    completion_window: Required[str]
    metadata: Dict[str, Any]
    idempotency_key: Optional[str]
