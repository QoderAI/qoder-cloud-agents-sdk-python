from __future__ import annotations

from typing import Any, Dict, Literal, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.types.channel_pairing import ChannelPairing
from qca.forward.types.deleted_channel_pairing import DeletedChannelPairing

__all__ = ["ChannelPairings", "AsyncChannelPairings"]


class ChannelPairings(SyncAPIResource):
    def retrieve(
        self,
        pairing_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelPairing:
        """GET /channel_pairings/{pairing_id}."""
        _path = path_template("/channel_pairings/{pairing_id}", pairing_id=pairing_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=ChannelPairing, options=options)

    def update(
        self,
        pairing_id: str,
        *,
        identity_id: Union[str, NotGiven] = NOT_GIVEN,
        template_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelPairing:
        """POST /channel_pairings/{pairing_id}. Provide at least one field; omitted fields retain their value."""
        _path = path_template("/channel_pairings/{pairing_id}", pairing_id=pairing_id)
        options = make_request_options(
            body={"identity_id": identity_id, "template_id": template_id},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=ChannelPairing, options=options)

    def list(
        self,
        *,
        channel_id: Union[str, NotGiven] = NOT_GIVEN,
        target_external_id: Union[str, NotGiven] = NOT_GIVEN,
        identity_id: Union[str, NotGiven] = NOT_GIVEN,
        template_id: Union[str, NotGiven] = NOT_GIVEN,
        after_id: Union[str, NotGiven] = NOT_GIVEN,
        before_id: Union[str, NotGiven] = NOT_GIVEN,
        status: Union[Literal["pairing", "active"], NotGiven] = NOT_GIVEN,
        target_type: Union[Literal["user", "group"], NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[ChannelPairing]:
        """GET /channel_pairings."""
        _path = path_template("/channel_pairings")
        options = make_request_options(
            body={},
            query={
                "channel_id": channel_id,
                "target_external_id": target_external_id,
                "identity_id": identity_id,
                "template_id": template_id,
                "after_id": after_id,
                "before_id": before_id,
                "status": status,
                "target_type": target_type,
                "limit": limit,
            },
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=ChannelPairing, options=options, page_style="Page")

    def create(
        self,
        *,
        code: Union[str, NotGiven] = NOT_GIVEN,
        channel_pairing_id: Union[str, NotGiven] = NOT_GIVEN,
        identity_id: str,
        template_id: str,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelPairing:
        """POST /channel_pairings.

        Supply exactly one of code or channel_pairing_id.
        """
        _path = path_template("/channel_pairings")
        options = make_request_options(
            body={
                "code": code,
                "channel_pairing_id": channel_pairing_id,
                "identity_id": identity_id,
                "template_id": template_id,
            },
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=ChannelPairing, options=options)

    def delete(
        self,
        pairing_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedChannelPairing:
        """DELETE /channel_pairings/{pairing_id}."""
        _path = path_template("/channel_pairings/{pairing_id}", pairing_id=pairing_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("DELETE", _path, cast_to=DeletedChannelPairing, options=options)


class AsyncChannelPairings(AsyncAPIResource):
    async def retrieve(
        self,
        pairing_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelPairing:
        """GET /channel_pairings/{pairing_id}."""
        _path = path_template("/channel_pairings/{pairing_id}", pairing_id=pairing_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=ChannelPairing, options=options)

    async def update(
        self,
        pairing_id: str,
        *,
        identity_id: Union[str, NotGiven] = NOT_GIVEN,
        template_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelPairing:
        """POST /channel_pairings/{pairing_id}. Provide at least one field; omitted fields retain their value."""
        _path = path_template("/channel_pairings/{pairing_id}", pairing_id=pairing_id)
        options = make_request_options(
            body={"identity_id": identity_id, "template_id": template_id},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=ChannelPairing, options=options)

    def list(
        self,
        *,
        channel_id: Union[str, NotGiven] = NOT_GIVEN,
        target_external_id: Union[str, NotGiven] = NOT_GIVEN,
        identity_id: Union[str, NotGiven] = NOT_GIVEN,
        template_id: Union[str, NotGiven] = NOT_GIVEN,
        after_id: Union[str, NotGiven] = NOT_GIVEN,
        before_id: Union[str, NotGiven] = NOT_GIVEN,
        status: Union[Literal["pairing", "active"], NotGiven] = NOT_GIVEN,
        target_type: Union[Literal["user", "group"], NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ChannelPairing]:
        """GET /channel_pairings."""
        _path = path_template("/channel_pairings")
        options = make_request_options(
            body={},
            query={
                "channel_id": channel_id,
                "target_external_id": target_external_id,
                "identity_id": identity_id,
                "template_id": template_id,
                "after_id": after_id,
                "before_id": before_id,
                "status": status,
                "target_type": target_type,
                "limit": limit,
            },
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=ChannelPairing, options=options, page_style="Page")
        )

    async def create(
        self,
        *,
        code: Union[str, NotGiven] = NOT_GIVEN,
        channel_pairing_id: Union[str, NotGiven] = NOT_GIVEN,
        identity_id: str,
        template_id: str,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelPairing:
        """POST /channel_pairings.

        Supply exactly one of code or channel_pairing_id.
        """
        _path = path_template("/channel_pairings")
        options = make_request_options(
            body={
                "code": code,
                "channel_pairing_id": channel_pairing_id,
                "identity_id": identity_id,
                "template_id": template_id,
            },
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=ChannelPairing, options=options)

    async def delete(
        self,
        pairing_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedChannelPairing:
        """DELETE /channel_pairings/{pairing_id}."""
        _path = path_template("/channel_pairings/{pairing_id}", pairing_id=pairing_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("DELETE", _path, cast_to=DeletedChannelPairing, options=options)
