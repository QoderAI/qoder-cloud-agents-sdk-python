from __future__ import annotations

from typing import Any, Dict, Optional, Union

from typing_extensions import TypedDict

from .model_config_param import ModelConfigParam

__all__ = ["SessionUpdateParamsConfigParam"]


class SessionUpdateParamsConfigParam(TypedDict, total=False):
    # Omit on create to inherit; None on update restores inheritance.
    model: Optional[Union[str, ModelConfigParam]]
    environment_variables: Dict[str, Any]
