from typing import Literal

from typing_extensions import TypedDict


class ChannelPairingListParams(TypedDict, total=False):
    channel_id: str
    status: Literal["pairing", "active"]
    target_type: Literal["user", "group"]
    target_external_id: str
    identity_id: str
    template_id: str
    limit: int
    after_id: str
    before_id: str
