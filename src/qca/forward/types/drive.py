from __future__ import annotations

from datetime import datetime
from typing import Literal

from typing_extensions import Required, TypedDict

from qca.common._models import BaseModel


class DriveEntry(BaseModel):
    path: str
    name: str
    type: Literal["file", "directory"]
    # Zero for an empty file; absent for directories.
    size: int | None = None
    etag: str | None = None
    last_modified: datetime | None = None


class DriveListEntriesResponse(BaseModel):
    """One page in service order; pass next_page_token unchanged to continue."""

    entries: list[DriveEntry]
    next_page_token: str | None = None


class DriveUploadURL(BaseModel):
    """Signed storage URL valid for 15 minutes. Treat url as a credential."""

    url: str
    method: Literal["PUT"]
    headers: dict[str, str]
    expires_at: datetime


class DriveDownloadURL(BaseModel):
    url: str
    method: Literal["GET"]
    headers: dict[str, str]
    expires_at: datetime
    # May be omitted for zero-byte files.
    size: int | None = None
    etag: str | None = None
    content_type: str | None = None


class DriveDeleteEntryResponse(BaseModel):
    deleted_count: int


class DriveClearResponse(BaseModel):
    deleted_count: int


class DriveListEntriesParams(TypedDict, total=False):
    identity_id: Required[str]
    path: str
    limit: int
    page_token: str


class DriveCreateUploadURLParams(TypedDict, total=False):
    identity_id: Required[str]
    path: Required[str]
    content_type: str
    idempotency_key: str


class DriveCreateDownloadURLParams(TypedDict, total=False):
    identity_id: Required[str]
    path: Required[str]
    idempotency_key: str


class DriveDeleteEntryParams(TypedDict, total=False):
    identity_id: Required[str]
    path: Required[str]
    recursive: bool


class DriveClearParams(TypedDict):
    identity_id: str
