from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .injection_location_params import InjectionLocationParams
    from .limited_credential_networking_params import LimitedCredentialNetworkingParams
    from .unrestricted_credential_networking_params import UnrestrictedCredentialNetworkingParams

__all__ = ["EnvironmentVariableCreateParams"]


class EnvironmentVariableCreateParams(TypedDict, total=False):
    networking: Required[Union[UnrestrictedCredentialNetworkingParams, LimitedCredentialNetworkingParams]]
    secret_name: Required[str]
    secret_value: Required[str]
    type: Required[Literal["environment_variable"]]
    injection_location: InjectionLocationParams
