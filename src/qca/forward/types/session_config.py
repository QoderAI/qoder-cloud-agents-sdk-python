from __future__ import annotations

from typing import Dict, Optional

from qca.common._models import BaseModel

__all__ = ["SessionConfig"]


class SessionConfig(BaseModel):
    environment_variables: Optional[Dict[str, str]] = None
