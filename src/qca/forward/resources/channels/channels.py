from __future__ import annotations

from functools import cached_property
from typing import Any, Dict, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.resources.channels.qr_sessions import AsyncQrSessions, QrSessions
from qca.forward.types.channel import Channel
from qca.forward.types.deleted_channel import DeletedChannel

__all__ = ["Channels", "AsyncChannels"]


class Channels(SyncAPIResource):
    @cached_property
    def qr_sessions(self) -> QrSessions:
        return QrSessions(self._client)

    def list(
        self,
        *,
        channel_type: Union[str, None, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
        binding_status: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Channel]:
        """GET /channels."""
        _path = path_template("/channels")
        options = make_request_options(
            body={},
            query={
                "channel_type": channel_type,
                "enabled": enabled,
                "binding_status": binding_status,
                "identity_id": identity_id,
                "template_id": template_id,
                "limit": limit,
                "after_id": after_id,
                "before_id": before_id,
            },
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Channel, options=options, page_style="Page")

    def create(
        self,
        *,
        channel_type: str,
        identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_resolution: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
        channel_config: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Channel:
        """POST /channels."""
        _path = path_template("/channels")
        options = make_request_options(
            body={
                "identity_id": identity_id,
                "identity_resolution": identity_resolution,
                "template_id": template_id,
                "channel_type": channel_type,
                "name": name,
                "enabled": enabled,
                "channel_config": channel_config,
            },
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Channel, options=options)

    def retrieve(
        self,
        channel_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Channel:
        """GET /channels/{channel_id}."""
        _path = path_template("/channels/{channel_id}", channel_id=channel_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Channel, options=options)

    def update(
        self,
        channel_id: str,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
        channel_config: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Channel:
        """POST /channels/{channel_id}."""
        _path = path_template("/channels/{channel_id}", channel_id=channel_id)
        options = make_request_options(
            body={
                "name": name,
                "identity_id": identity_id,
                "template_id": template_id,
                "enabled": enabled,
                "channel_config": channel_config,
            },
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Channel, options=options)

    def delete(
        self,
        channel_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedChannel:
        """DELETE /channels/{channel_id}."""
        _path = path_template("/channels/{channel_id}", channel_id=channel_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("DELETE", _path, cast_to=DeletedChannel, options=options)


class AsyncChannels(AsyncAPIResource):
    @cached_property
    def qr_sessions(self) -> AsyncQrSessions:
        return AsyncQrSessions(self._client)

    def list(
        self,
        *,
        channel_type: Union[str, None, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
        binding_status: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Channel]:
        """GET /channels."""
        _path = path_template("/channels")
        options = make_request_options(
            body={},
            query={
                "channel_type": channel_type,
                "enabled": enabled,
                "binding_status": binding_status,
                "identity_id": identity_id,
                "template_id": template_id,
                "limit": limit,
                "after_id": after_id,
                "before_id": before_id,
            },
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=Channel, options=options, page_style="Page")
        )

    async def create(
        self,
        *,
        channel_type: str,
        identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_resolution: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
        channel_config: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Channel:
        """POST /channels."""
        _path = path_template("/channels")
        options = make_request_options(
            body={
                "identity_id": identity_id,
                "identity_resolution": identity_resolution,
                "template_id": template_id,
                "channel_type": channel_type,
                "name": name,
                "enabled": enabled,
                "channel_config": channel_config,
            },
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Channel, options=options)

    async def retrieve(
        self,
        channel_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Channel:
        """GET /channels/{channel_id}."""
        _path = path_template("/channels/{channel_id}", channel_id=channel_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=Channel, options=options)

    async def update(
        self,
        channel_id: str,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
        channel_config: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Channel:
        """POST /channels/{channel_id}."""
        _path = path_template("/channels/{channel_id}", channel_id=channel_id)
        options = make_request_options(
            body={
                "name": name,
                "identity_id": identity_id,
                "template_id": template_id,
                "enabled": enabled,
                "channel_config": channel_config,
            },
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Channel, options=options)

    async def delete(
        self,
        channel_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedChannel:
        """DELETE /channels/{channel_id}."""
        _path = path_template("/channels/{channel_id}", channel_id=channel_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("DELETE", _path, cast_to=DeletedChannel, options=options)
