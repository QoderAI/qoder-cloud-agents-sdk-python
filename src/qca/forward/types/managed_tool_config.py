from qca.common._models import BaseModel


class ManagedToolConfig(BaseModel):
    """Forward-managed tools, distinct from tools[].enabled_tools."""

    enabled_tools: list[str]
