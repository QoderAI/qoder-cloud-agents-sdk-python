from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Union

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .deployment_user_define_outcome_event_rubric_union import DeploymentUserDefineOutcomeEventRubricUnion
    from .deployment_user_message_event_content_union import DeploymentUserMessageEventContentUnion
    from .system_content_block import SystemContentBlock

__all__ = ["DeploymentInitialEventUnion"]


class DeploymentInitialEventUnion(BaseModel):
    content: Optional[Union[List[DeploymentUserMessageEventContentUnion], List[SystemContentBlock]]] = None
    type: Optional[str] = None
    description: Optional[str] = None
    rubric: Optional[DeploymentUserDefineOutcomeEventRubricUnion] = None
    max_iterations: Optional[int] = None
