from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["GitHubRepositoryResourceConfigCheckoutUnion"]


class GitHubRepositoryResourceConfigCheckoutUnion(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    sha: Optional[str] = None
