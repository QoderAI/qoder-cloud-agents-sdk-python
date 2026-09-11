from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["GitHubRepositoryParam"]


class GitHubRepositoryParam(TypedDict, total=False):
    url: Optional[str]
    mount_path: Optional[str]
    enabled: Optional[bool]
    authorization_token: Optional[str]
