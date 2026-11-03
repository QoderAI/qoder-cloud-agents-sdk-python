from __future__ import annotations

from typing import Any, Dict, Union

from typing_extensions import TypedDict

from .model_config_param import ModelConfigParam

__all__ = ["SessionCreateParamsConfigParam"]


class SessionCreateParamsConfigParam(TypedDict, total=False):
    # Omit on create to inherit; None on update restores inheritance.
    model: Union[str, ModelConfigParam]
    environment_variables: Dict[str, Any]
