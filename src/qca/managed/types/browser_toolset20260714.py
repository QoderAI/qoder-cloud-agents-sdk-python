from typing import Literal

from qca.common._models import BaseModel

__all__ = ["BrowserToolset20260714"]


class BrowserToolset20260714(BaseModel):
    """Browser snapshot; future response fields remain available as extras."""

    type: Literal["browser_toolset_20260714"]
