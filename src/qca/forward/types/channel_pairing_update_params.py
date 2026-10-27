from typing_extensions import TypedDict


class ChannelPairingUpdateParams(TypedDict, total=False):
    """Provide at least one nonempty field; omitted fields retain their value."""

    identity_id: str
    template_id: str
