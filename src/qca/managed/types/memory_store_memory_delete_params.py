from __future__ import annotations

from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["MemoryStoreMemoryDeleteParams"]


class MemoryStoreMemoryDeleteParams(TypedDict, total=False):
    expected_content_sha256: Optional[str]
    workspace_id: Optional[str]
    betas: List[str]
