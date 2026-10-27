from typing_extensions import Required, TypedDict


class IdentityMemoryStoreListParams(TypedDict, total=False):
    identity_id: Required[str]
    limit: int
    after_id: str
    before_id: str
