from __future__ import annotations

from typing import Any, Dict, Optional, Union

from typing_extensions import TypedDict

from .model_config_param import ModelConfigParam
from .multiagent_config_param import MultiagentConfigParam

__all__ = ["SessionUpdateParamsConfigParam"]


class SessionUpdateParamsConfigParam(TypedDict, total=False):
    # Omit on create to inherit; None on update restores inheritance.
    model: Optional[Union[str, ModelConfigParam]]
    environment_variables: Dict[str, Any]
    multiagent: Optional[MultiagentConfigParam]
    """Omit to keep the roster; None clears it without restoring inheritance."""
