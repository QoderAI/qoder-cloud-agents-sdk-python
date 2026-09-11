from __future__ import annotations

from typing import Any, Dict, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.types.batch_task import BatchTask

__all__ = ["Tasks", "AsyncTasks"]


class Tasks(SyncAPIResource):
    def list(
        self,
        batch_id: str,
        *,
        status: Union[str, None, NotGiven] = NOT_GIVEN,
        custom_id: Union[str, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[BatchTask]:
        """GET /batches/{batch_id}/tasks."""
        _path = path_template("/batches/{batch_id}/tasks", batch_id=batch_id)
        options = make_request_options(
            body={},
            query={"status": status, "custom_id": custom_id, "limit": limit, "after_id": after_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=BatchTask, options=options, page_style="Page")


class AsyncTasks(AsyncAPIResource):
    def list(
        self,
        batch_id: str,
        *,
        status: Union[str, None, NotGiven] = NOT_GIVEN,
        custom_id: Union[str, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BatchTask]:
        """GET /batches/{batch_id}/tasks."""
        _path = path_template("/batches/{batch_id}/tasks", batch_id=batch_id)
        options = make_request_options(
            body={},
            query={"status": status, "custom_id": custom_id, "limit": limit, "after_id": after_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=BatchTask, options=options, page_style="Page")
        )
