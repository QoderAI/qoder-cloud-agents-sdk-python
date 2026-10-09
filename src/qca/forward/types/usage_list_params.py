from typing import List, Union

from typing_extensions import Required, TypedDict


class UsageListParams(TypedDict, total=False):
    """Hourly Asia/Shanghai window, including CN and Global. No legacy timestamp parameters."""

    start_at: Required[str]
    end_at: Required[str]
    limit: int
    after_id: str
    before_id: str
    identity_id: str
    identity_ids: Union[str, List[str]]
    template_id: str
    template_ids: Union[str, List[str]]
