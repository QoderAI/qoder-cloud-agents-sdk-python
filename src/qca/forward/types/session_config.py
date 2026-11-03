from __future__ import annotations

from typing import Dict, Optional, Union

from qca.common._models import BaseModel

from .model_config import ModelConfig

__all__ = ["SessionConfig"]


class SessionConfig(BaseModel):
    model: Optional[Union[str, ModelConfig]] = None
    environment_variables: Optional[Dict[str, str]] = None
