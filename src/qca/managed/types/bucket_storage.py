from typing import List, Literal, Optional, Union

from typing_extensions import Required, TypedDict

from qca.common._models import BaseModel


class OSSRAMRoleCredentialParam(TypedDict, total=False):
    type: Required[Literal["ram_role"]]
    # Required for a new bucket; omit to retain a stored credential on update.
    role_arn: str


class OSSAccessKeyCredentialParam(TypedDict, total=False):
    type: Required[Literal["access_key"]]
    access_key_id: Required[str]
    # Required for a new key; omitted when echoing a masked credential on update.
    access_key_secret: str


OSSBucketCredentialParam = Union[OSSRAMRoleCredentialParam, OSSAccessKeyCredentialParam]


class OSSBucketParam(TypedDict, total=False):
    name: Required[str]
    provider: Required[Literal["aliyun-oss"]]
    region: Required[str]
    bucket: Required[str]
    prefix: str
    access: Literal["read_only", "read_write"]
    accelerator_endpoint: str
    credential: OSSBucketCredentialParam


class BucketStorageParam(TypedDict):
    buckets: List[OSSBucketParam]


class OSSBucketCredential(BaseModel):
    """Read view; the API never returns role ARN or AccessKey secret."""

    type: Literal["ram_role", "access_key"]
    access_key_id: Optional[str] = None


class OSSBucket(BaseModel):
    name: str
    provider: Literal["aliyun-oss"]
    region: str
    bucket: str
    prefix: Optional[str] = None
    access: Optional[Literal["read_only", "read_write"]] = None
    accelerator_endpoint: Optional[str] = None
    credential: Optional[OSSBucketCredential] = None


class BucketStorage(BaseModel):
    buckets: List[OSSBucket]
