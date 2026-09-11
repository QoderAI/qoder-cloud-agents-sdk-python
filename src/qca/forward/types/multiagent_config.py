from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .multiagent_entry import MultiagentEntry

__all__ = ["MultiagentConfig"]


class MultiagentConfig(BaseModel):
    type: Optional[str] = None
    agents: Optional[List[MultiagentEntry]] = None
