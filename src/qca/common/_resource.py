from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ._response import RawResponseResource

if TYPE_CHECKING:
    from ._base_client import AsyncAPIClient, SyncAPIClient


class SyncAPIResource:
    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    @cached_property
    def with_raw_response(self) -> RawResponseResource:
        return RawResponseResource(self)

    @cached_property
    def with_streaming_response(self) -> RawResponseResource:
        return RawResponseResource(self, streaming=True)


class AsyncAPIResource:
    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    @cached_property
    def with_raw_response(self) -> RawResponseResource:
        return RawResponseResource(self)

    @cached_property
    def with_streaming_response(self) -> RawResponseResource:
        return RawResponseResource(self, streaming=True)
