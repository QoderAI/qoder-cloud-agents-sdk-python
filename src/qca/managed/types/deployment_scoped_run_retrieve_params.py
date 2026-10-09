from typing import List

from typing_extensions import Required, TypedDict


class DeploymentScopedRunRetrieveParams(TypedDict, total=False):
    deployment_id: Required[str]
    workspace_id: str
    betas: List[str]
