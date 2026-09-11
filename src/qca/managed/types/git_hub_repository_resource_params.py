from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Optional, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .branch_checkout_param import BranchCheckoutParam
    from .commit_checkout_param import CommitCheckoutParam

__all__ = ["GitHubRepositoryResourceParams"]


class GitHubRepositoryResourceParams(TypedDict, total=False):
    authorization_token: Required[str]
    type: Required[Literal["github_repository"]]
    url: Required[str]
    mount_path: Optional[str]
    checkout: Union[BranchCheckoutParam, CommitCheckoutParam]
