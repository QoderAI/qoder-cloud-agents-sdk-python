from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Optional, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .effort_high_param import EffortHighParam
    from .effort_low_param import EffortLowParam
    from .effort_max_param import EffortMaxParam
    from .effort_medium_param import EffortMediumParam
    from .effort_xhigh_param import EffortXhighParam

__all__ = ["ModelConfigParams"]


class ModelConfigParams(TypedDict, total=False):
    context_window: Optional[int]
    id: Required[
        Literal[
            "claude-fable-5-1",
            "claude-sonnet-5",
            "claude-fable-5",
            "claude-opus-5",
            "claude-opus-4-8",
            "claude-opus-4-7",
            "claude-opus-4-6",
            "claude-sonnet-4-6",
            "claude-haiku-4-5",
            "claude-haiku-4-5-20251001",
            "claude-opus-4-5",
            "claude-opus-4-5-20251101",
            "claude-sonnet-4-5",
            "claude-sonnet-4-5-20250929",
        ]
    ]
    inference_geo: Optional[str]
    effort: Union[str, EffortLowParam, EffortMediumParam, EffortHighParam, EffortXhighParam, EffortMaxParam]
    speed: Literal["standard", "fast"]
