from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["TemplateCloneParams"]


class TemplateCloneParams(TypedDict, total=False):
    name: Optional[str]
    description: Optional[str]
    idempotency_key: Optional[str]
