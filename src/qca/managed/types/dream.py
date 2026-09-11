from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .dream_error import DreamError
    from .dream_input_union import DreamInputUnion
    from .dream_model_config import DreamModelConfig
    from .dream_output import DreamOutput
    from .dream_usage import DreamUsage
    from .output_behavior_union import OutputBehaviorUnion

__all__ = ["Dream"]


class Dream(BaseModel):
    id: Optional[str] = None
    archived_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
    error: Optional[DreamError] = None
    inputs: Optional[List[DreamInputUnion]] = None
    instructions: Optional[str] = None
    model: Optional[DreamModelConfig] = None
    output_behavior: Optional[OutputBehaviorUnion] = None
    outputs: Optional[List[DreamOutput]] = None
    session_id: Optional[str] = None
    status: Optional[str] = None
    type: Optional[str] = None
    usage: Optional[DreamUsage] = None
