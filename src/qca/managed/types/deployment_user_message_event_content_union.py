from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .deployment_user_message_event_content_union_source import DeploymentUserMessageEventContentUnionSource

__all__ = ["DeploymentUserMessageEventContentUnion"]


class DeploymentUserMessageEventContentUnion(BaseModel):
    text: Optional[str] = None
    type: Optional[str] = None
    source: Optional[DeploymentUserMessageEventContentUnionSource] = None
    context: Optional[str] = None
    title: Optional[str] = None
