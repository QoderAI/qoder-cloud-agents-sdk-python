from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Optional, Union

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from .limited_network_params import LimitedNetworkParams
    from .packages_params import PackagesParams
    from .unrestricted_network_param import UnrestrictedNetworkParam

__all__ = ["CloudConfigParams"]


class CloudConfigParams(TypedDict, total=False):
    setup_script: Optional[str]
    networking: Union[UnrestrictedNetworkParam, LimitedNetworkParams]
    packages: PackagesParams
    type: Literal["cloud"]
