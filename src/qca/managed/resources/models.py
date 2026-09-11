from __future__ import annotations

from typing import Any, Dict, List, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.managed.types.model_info import ModelInfo

__all__ = ["Models", "AsyncModels"]


class Models(SyncAPIResource):
    def list(
        self,
        *,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[ModelInfo]:
        """GET /models."""
        _path = path_template("/models")
        options = make_request_options(
            body={},
            query={"after_id": after_id, "before_id": before_id, "limit": limit},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=ModelInfo, options=options, page_style="Page")


class AsyncModels(AsyncAPIResource):
    def list(
        self,
        *,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ModelInfo]:
        """GET /models."""
        _path = path_template("/models")
        options = make_request_options(
            body={},
            query={"after_id": after_id, "before_id": before_id, "limit": limit},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=ModelInfo, options=options, page_style="Page")
        )
