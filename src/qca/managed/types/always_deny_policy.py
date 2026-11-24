from typing import Literal

from qca.common._models import BaseModel

__all__ = ["AlwaysDenyPolicy"]


class AlwaysDenyPolicy(BaseModel):
    type: Literal["always_deny"]
