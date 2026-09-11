from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .git_hub_repository_resource_checkout_union import GitHubRepositoryResourceCheckoutUnion

__all__ = ["SessionResourceUnion"]


class SessionResourceUnion(BaseModel):
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    mount_path: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[datetime] = None
    url: Optional[str] = None
    checkout: Optional[GitHubRepositoryResourceCheckoutUnion] = None
    file_id: Optional[str] = None
    memory_store_id: Optional[str] = None
    access: Optional[str] = None
    description: Optional[str] = None
    instructions: Optional[str] = None
    name: Optional[str] = None
