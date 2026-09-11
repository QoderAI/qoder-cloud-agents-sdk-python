from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .git_hub_repository_resource_config_checkout_union import GitHubRepositoryResourceConfigCheckoutUnion

__all__ = ["SessionResourceConfigUnion"]


class SessionResourceConfigUnion(BaseModel):
    type: Optional[str] = None
    url: Optional[str] = None
    checkout: Optional[GitHubRepositoryResourceConfigCheckoutUnion] = None
    mount_path: Optional[str] = None
    file_id: Optional[str] = None
    memory_store_id: Optional[str] = None
    access: Optional[str] = None
    instructions: Optional[str] = None
