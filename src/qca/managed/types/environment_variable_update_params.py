from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Optional, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .injection_location_update_params import InjectionLocationUpdateParams
    from .limited_credential_networking_params import LimitedCredentialNetworkingParams
    from .unrestricted_credential_networking_params import UnrestrictedCredentialNetworkingParams

__all__ = ["EnvironmentVariableUpdateParams"]


class EnvironmentVariableUpdateParams(TypedDict, total=False):
    type: Required[Literal["environment_variable"]]
    secret_value: Optional[str]
    injection_location: InjectionLocationUpdateParams
    networking: Union[UnrestrictedCredentialNetworkingParams, LimitedCredentialNetworkingParams]
