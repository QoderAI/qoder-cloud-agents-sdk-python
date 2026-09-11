from __future__ import annotations

from typing import Optional

from typing_extensions import Required, TypedDict

__all__ = ["MultiagentEntryParam"]


class MultiagentEntryParam(TypedDict, total=False):
    type: Required[str]
    template_id: Optional[str]
    name: Optional[str]
