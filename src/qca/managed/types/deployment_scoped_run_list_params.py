from typing import List

from typing_extensions import Required, TypedDict


class DeploymentScopedRunListParams(TypedDict, total=False):
    deployment_id: Required[str]
    limit: int
    page: str
    after_id: str
    before_id: str
    triggered_after: str
    triggered_before: str
    workspace_id: str
    betas: List[str]
