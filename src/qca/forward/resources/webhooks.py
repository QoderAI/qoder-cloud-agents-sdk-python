from __future__ import annotations

from functools import cached_property
from typing import Any, Dict, List, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.types.webhook_endpoint import (
    WebhookEndpoint,
    WebhookEndpointCreateResponse,
    WebhookEndpointTestResponse,
)


class Webhooks(SyncAPIResource):
    @cached_property
    def endpoints(self) -> WebhookEndpoints:
        return WebhookEndpoints(self._client)


class WebhookEndpoints(SyncAPIResource):
    def create(
        self,
        *,
        url: str,
        events: List[str],
        description: Union[str, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str], NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookEndpointCreateResponse:
        """POST /webhook/endpoints. Requires a PAT or administrator SAT."""
        _path = path_template("/webhook/endpoints")
        options = make_request_options(
            body={"url": url, "events": events, "description": description, "metadata": metadata},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=WebhookEndpointCreateResponse, options=options)

    def list(
        self,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        after_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[WebhookEndpoint]:
        """GET /webhook/endpoints. Requires a PAT or administrator SAT."""
        _path = path_template("/webhook/endpoints")
        options = make_request_options(
            body={},
            query={"limit": limit, "after_id": after_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=WebhookEndpoint, options=options, page_style="Page")

    def retrieve(
        self,
        endpoint_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookEndpoint:
        """GET /webhook/endpoints/{endpoint_id}. Requires a PAT or administrator SAT."""
        _path = path_template("/webhook/endpoints/{endpoint_id}", endpoint_id=endpoint_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=WebhookEndpoint, options=options)

    def update(
        self,
        endpoint_id: str,
        *,
        url: Union[str, NotGiven] = NOT_GIVEN,
        events: Union[List[str], NotGiven] = NOT_GIVEN,
        description: Union[str, NotGiven] = NOT_GIVEN,
        active: Union[bool, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str | None], NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookEndpoint:
        """PUT /webhook/endpoints/{endpoint_id}. Requires a PAT or administrator SAT."""
        _path = path_template("/webhook/endpoints/{endpoint_id}", endpoint_id=endpoint_id)
        options = make_request_options(
            body={"url": url, "events": events, "description": description, "active": active, "metadata": metadata},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("PUT", _path, cast_to=WebhookEndpoint, options=options)

    def delete(
        self,
        endpoint_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """DELETE /webhook/endpoints/{endpoint_id}. Requires a PAT or administrator SAT."""
        _path = path_template("/webhook/endpoints/{endpoint_id}", endpoint_id=endpoint_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if extra_body is None:
            options["body"] = None
        return self._client.request("DELETE", _path, cast_to=None, options=options)

    def enable(
        self,
        endpoint_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookEndpoint:
        """POST /webhook/endpoints/{endpoint_id}/enable. Requires a PAT or administrator SAT."""
        _path = path_template("/webhook/endpoints/{endpoint_id}/enable", endpoint_id=endpoint_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if extra_body is None:
            options["body"] = None
        return self._client.request("POST", _path, cast_to=WebhookEndpoint, options=options)

    def disable(
        self,
        endpoint_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookEndpoint:
        """POST /webhook/endpoints/{endpoint_id}/disable. Requires a PAT or administrator SAT."""
        _path = path_template("/webhook/endpoints/{endpoint_id}/disable", endpoint_id=endpoint_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if extra_body is None:
            options["body"] = None
        return self._client.request("POST", _path, cast_to=WebhookEndpoint, options=options)

    def test(
        self,
        endpoint_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookEndpointTestResponse:
        """POST /webhook/endpoints/{endpoint_id}/test. Queues a test event; 202 does not confirm delivery."""
        _path = path_template("/webhook/endpoints/{endpoint_id}/test", endpoint_id=endpoint_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if extra_body is None:
            options["body"] = None
        return self._client.request("POST", _path, cast_to=WebhookEndpointTestResponse, options=options)


class AsyncWebhooks(AsyncAPIResource):
    @cached_property
    def endpoints(self) -> AsyncWebhookEndpoints:
        return AsyncWebhookEndpoints(self._client)


class AsyncWebhookEndpoints(AsyncAPIResource):
    async def create(
        self,
        *,
        url: str,
        events: List[str],
        description: Union[str, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str], NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookEndpointCreateResponse:
        """POST /webhook/endpoints. Requires a PAT or administrator SAT."""
        _path = path_template("/webhook/endpoints")
        options = make_request_options(
            body={"url": url, "events": events, "description": description, "metadata": metadata},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=WebhookEndpointCreateResponse, options=options)

    def list(
        self,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        after_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WebhookEndpoint]:
        """GET /webhook/endpoints. Requires a PAT or administrator SAT."""
        _path = path_template("/webhook/endpoints")
        options = make_request_options(
            body={},
            query={"limit": limit, "after_id": after_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=WebhookEndpoint, options=options, page_style="Page")
        )

    async def retrieve(
        self,
        endpoint_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookEndpoint:
        """GET /webhook/endpoints/{endpoint_id}. Requires a PAT or administrator SAT."""
        _path = path_template("/webhook/endpoints/{endpoint_id}", endpoint_id=endpoint_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=WebhookEndpoint, options=options)

    async def update(
        self,
        endpoint_id: str,
        *,
        url: Union[str, NotGiven] = NOT_GIVEN,
        events: Union[List[str], NotGiven] = NOT_GIVEN,
        description: Union[str, NotGiven] = NOT_GIVEN,
        active: Union[bool, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str | None], NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookEndpoint:
        """PUT /webhook/endpoints/{endpoint_id}. Requires a PAT or administrator SAT."""
        _path = path_template("/webhook/endpoints/{endpoint_id}", endpoint_id=endpoint_id)
        options = make_request_options(
            body={"url": url, "events": events, "description": description, "active": active, "metadata": metadata},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("PUT", _path, cast_to=WebhookEndpoint, options=options)

    async def delete(
        self,
        endpoint_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """DELETE /webhook/endpoints/{endpoint_id}. Requires a PAT or administrator SAT."""
        _path = path_template("/webhook/endpoints/{endpoint_id}", endpoint_id=endpoint_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if extra_body is None:
            options["body"] = None
        return await self._client.request("DELETE", _path, cast_to=None, options=options)

    async def enable(
        self,
        endpoint_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookEndpoint:
        """POST /webhook/endpoints/{endpoint_id}/enable. Requires a PAT or administrator SAT."""
        _path = path_template("/webhook/endpoints/{endpoint_id}/enable", endpoint_id=endpoint_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if extra_body is None:
            options["body"] = None
        return await self._client.request("POST", _path, cast_to=WebhookEndpoint, options=options)

    async def disable(
        self,
        endpoint_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookEndpoint:
        """POST /webhook/endpoints/{endpoint_id}/disable. Requires a PAT or administrator SAT."""
        _path = path_template("/webhook/endpoints/{endpoint_id}/disable", endpoint_id=endpoint_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if extra_body is None:
            options["body"] = None
        return await self._client.request("POST", _path, cast_to=WebhookEndpoint, options=options)

    async def test(
        self,
        endpoint_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookEndpointTestResponse:
        """POST /webhook/endpoints/{endpoint_id}/test. Queues a test event; 202 does not confirm delivery."""
        _path = path_template("/webhook/endpoints/{endpoint_id}/test", endpoint_id=endpoint_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if extra_body is None:
            options["body"] = None
        return await self._client.request("POST", _path, cast_to=WebhookEndpointTestResponse, options=options)
