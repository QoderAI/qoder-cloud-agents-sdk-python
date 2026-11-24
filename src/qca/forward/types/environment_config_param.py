from typing import List, Literal

from typing_extensions import Required, TypedDict

from .bucket_storage import BucketStorageParam

__all__ = ["EnvironmentConfigParam", "EnvironmentConfigPackagesParam"]


class EnvironmentConfigPackagesParam(TypedDict, total=False):
    apt: List[str]
    cargo: List[str]
    gem: List[str]
    go: List[str]
    npm: List[str]
    pip: List[str]


class EnvironmentConfigParam(TypedDict, total=False):
    """The entire config replaces the previous config on update.

    Cloud storage supports up to seven mounts, gated by oss-bucket-2026-09-23.
    buckets=[] removes mounts for future Sessions, not existing snapshots.
    """

    type: Required[Literal["cloud", "self_hosted"]]
    setup_script: str
    startup_script: str
    packages: EnvironmentConfigPackagesParam
    storage: BucketStorageParam
