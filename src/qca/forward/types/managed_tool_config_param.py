from typing_extensions import TypedDict


class ManagedToolConfigParam(TypedDict):
    """Replaces the complete enabled list; [] disables all managed tools."""

    enabled_tools: list[str]
