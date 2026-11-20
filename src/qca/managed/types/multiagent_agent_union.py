from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Union

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .model_config import ModelConfig

__all__ = ["MultiagentAgentUnion"]


class MultiagentAgentUnion(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    # A saved child Agent version: a concrete version or "latest".
    version: Optional[Union[int, str]] = None
    model: Optional[Union[str, ModelConfig]] = None
