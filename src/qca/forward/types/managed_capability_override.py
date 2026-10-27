from typing_extensions import TypedDict

from qca.common._models import BaseModel


class ManagedCapabilityOverrideParam(TypedDict):
    enabled: bool


class ManagedCapabilityOverride(BaseModel):
    enabled: bool
