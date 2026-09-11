from __future__ import annotations

from typing import Any, Dict, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.forward.types.session_resource import SessionResource

__all__ = ["Resources", "AsyncResources"]


class Resources(SyncAPIResource):
    def add(
        self,
        session_id: str,
        *,
        type: str,
        file_id: str,
        mount_path: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionResource:
        """POST /sessions/{session_id}/resources."""
        _path = path_template("/sessions/{session_id}/resources", session_id=session_id)
        options = make_request_options(
            body={"type": type, "file_id": file_id, "mount_path": mount_path},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=SessionResource, options=options)


class AsyncResources(AsyncAPIResource):
    async def add(
        self,
        session_id: str,
        *,
        type: str,
        file_id: str,
        mount_path: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionResource:
        """POST /sessions/{session_id}/resources."""
        _path = path_template("/sessions/{session_id}/resources", session_id=session_id)
        options = make_request_options(
            body={"type": type, "file_id": file_id, "mount_path": mount_path},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=SessionResource, options=options)
