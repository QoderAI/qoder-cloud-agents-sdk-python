from __future__ import annotations

from typing import Any, Dict, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.managed.types.oauth_start_response import OAuthStartResponse


class OAuth(SyncAPIResource):
    def start(
        self,
        *,
        vault_id: str,
        mcp_server_url: str,
        client_id: Union[str, NotGiven] = NOT_GIVEN,
        client_secret: Union[str, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OAuthStartResponse:
        """POST /oauth/start. Returns a browser authorization URL; this call does not complete authorization."""
        _path = path_template("/oauth/start")
        options = make_request_options(
            body={
                "vault_id": vault_id,
                "mcp_server_url": mcp_server_url,
                "client_id": client_id,
                "client_secret": client_secret,
            },
            query={},
            headers={"qoder-workspace-id": workspace_id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=OAuthStartResponse, options=options)


class AsyncOAuth(AsyncAPIResource):
    async def start(
        self,
        *,
        vault_id: str,
        mcp_server_url: str,
        client_id: Union[str, NotGiven] = NOT_GIVEN,
        client_secret: Union[str, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OAuthStartResponse:
        """POST /oauth/start. Returns a browser authorization URL; this call does not complete authorization."""
        _path = path_template("/oauth/start")
        options = make_request_options(
            body={
                "vault_id": vault_id,
                "mcp_server_url": mcp_server_url,
                "client_id": client_id,
                "client_secret": client_secret,
            },
            query={},
            headers={"qoder-workspace-id": workspace_id},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=OAuthStartResponse, options=options)
