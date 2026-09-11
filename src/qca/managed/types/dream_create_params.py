from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .dream_memory_store_input_param import DreamMemoryStoreInputParam
    from .dream_model_config_param import DreamModelConfigParam
    from .dream_sessions_input_param import DreamSessionsInputParam
    from .output_behavior_create_new_param import OutputBehaviorCreateNewParam
    from .output_behavior_update_existing_param import OutputBehaviorUpdateExistingParam

__all__ = ["DreamCreateParams"]


class DreamCreateParams(TypedDict, total=False):
    inputs: Required[List[Union[DreamMemoryStoreInputParam, DreamSessionsInputParam]]]
    model: Required[Union[str, DreamModelConfigParam]]
    instructions: Optional[str]
    workspace_id: Optional[str]
    output_behavior: Union[OutputBehaviorCreateNewParam, OutputBehaviorUpdateExistingParam]
    betas: List[str]
