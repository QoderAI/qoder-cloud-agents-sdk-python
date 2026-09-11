from __future__ import annotations

from typing import Any, Dict, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.forward.types.channel_pairing import ChannelPairing
from qca.forward.types.deleted_channel_pairing import DeletedChannelPairing

__all__ = ["ChannelPairings", "AsyncChannelPairings"]


class ChannelPairings(SyncAPIResource):
    def create(
        self,
        *,
        code: str,
        identity_id: str,
        template_id: str,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelPairing:
        """POST /channel_pairings."""
        _path = path_template("/channel_pairings")
        options = make_request_options(
            body={"code": code, "identity_id": identity_id, "template_id": template_id},
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
    async def create(
        self,
        *,
        code: str,
        identity_id: str,
        template_id: str,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelPairing:
        """POST /channel_pairings."""
        _path = path_template("/channel_pairings")
        options = make_request_options(
            body={"code": code, "identity_id": identity_id, "template_id": template_id},
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
