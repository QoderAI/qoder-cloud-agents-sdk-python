from typing import Literal, Optional

from typing_extensions import Required, TypedDict

__all__ = ["ModelConfigParams"]


class ModelConfigParams(TypedDict, total=False):
    inference_geo: Optional[str]
    id: Required[str]
    effort: Literal["none", "low", "medium", "high", "xhigh", "max"]
    context_window: int
