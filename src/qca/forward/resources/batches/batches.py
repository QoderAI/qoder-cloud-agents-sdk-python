from __future__ import annotations

from functools import cached_property
from typing import Any, Dict, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.resources.batches.tasks import AsyncTasks, Tasks
from qca.forward.types.batch import Batch
from qca.forward.types.batch_file import BatchFile

__all__ = ["Batches", "AsyncBatches"]


class Batches(SyncAPIResource):
    @cached_property
    def tasks(self) -> Tasks:
        return Tasks(self._client)

    def list(
        self,
        *,
        status: Union[str, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Batch]:
        """GET /batches."""
        _path = path_template("/batches")
        options = make_request_options(
            body={},
            query={"status": status, "limit": limit, "after_id": after_id, "before_id": before_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Batch, options=options, page_style="Page")

    def create(
        self,
        *,
        input_file_id: str,
        completion_window: str,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Batch:
        """POST /batches."""
        _path = path_template("/batches")
        options = make_request_options(
            body={"input_file_id": input_file_id, "completion_window": completion_window, "metadata": metadata},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Batch, options=options)

    def retrieve(
        self,
        batch_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Batch:
        """GET /batches/{batch_id}."""
        _path = path_template("/batches/{batch_id}", batch_id=batch_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Batch, options=options)

    def cancel(
        self,
        batch_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Batch:
        """POST /batches/{batch_id}/cancel."""
        _path = path_template("/batches/{batch_id}/cancel", batch_id=batch_id)
        options = make_request_options(
            body={},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Batch, options=options)

    def retrieve_error(
        self,
        batch_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchFile:
        """GET /batches/{batch_id}/error."""
        _path = path_template("/batches/{batch_id}/error", batch_id=batch_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=BatchFile, options=options)

    def retrieve_output(
        self,
        batch_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchFile:
        """GET /batches/{batch_id}/output."""
        _path = path_template("/batches/{batch_id}/output", batch_id=batch_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=BatchFile, options=options)


class AsyncBatches(AsyncAPIResource):
    @cached_property
    def tasks(self) -> AsyncTasks:
        return AsyncTasks(self._client)

    def list(
        self,
        *,
        status: Union[str, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Batch]:
        """GET /batches."""
        _path = path_template("/batches")
        options = make_request_options(
            body={},
            query={"status": status, "limit": limit, "after_id": after_id, "before_id": before_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=Batch, options=options, page_style="Page")
        )

    async def create(
        self,
        *,
        input_file_id: str,
        completion_window: str,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Batch:
        """POST /batches."""
        _path = path_template("/batches")
        options = make_request_options(
            body={"input_file_id": input_file_id, "completion_window": completion_window, "metadata": metadata},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Batch, options=options)

    async def retrieve(
        self,
        batch_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Batch:
        """GET /batches/{batch_id}."""
        _path = path_template("/batches/{batch_id}", batch_id=batch_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=Batch, options=options)

    async def cancel(
        self,
        batch_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Batch:
        """POST /batches/{batch_id}/cancel."""
        _path = path_template("/batches/{batch_id}/cancel", batch_id=batch_id)
        options = make_request_options(
            body={},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Batch, options=options)

    async def retrieve_error(
        self,
        batch_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchFile:
        """GET /batches/{batch_id}/error."""
        _path = path_template("/batches/{batch_id}/error", batch_id=batch_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=BatchFile, options=options)

    async def retrieve_output(
        self,
        batch_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchFile:
        """GET /batches/{batch_id}/output."""
        _path = path_template("/batches/{batch_id}/output", batch_id=batch_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=BatchFile, options=options)
