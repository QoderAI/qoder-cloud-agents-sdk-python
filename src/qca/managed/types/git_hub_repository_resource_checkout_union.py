from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["GitHubRepositoryResourceCheckoutUnion"]


class GitHubRepositoryResourceCheckoutUnion(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    sha: Optional[str] = None
