from __future__ import annotations

from typing import Any

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.forward.resources._service_account_auth import sa_key_headers
from qca.forward.types.service_account_token import ServiceAccountToken

__all__ = ["ServiceAccountTokens", "AsyncServiceAccountTokens"]


class ServiceAccountTokens(SyncAPIResource):
    def create(
        self,
        identity_id: str,
        *,
        sa_key: str,
        ttl_seconds: int | NotGiven = NOT_GIVEN,
        metadata: dict[str, Any] | NotGiven = NOT_GIVEN,
        extra_headers: dict[str, str] | None = None,
        extra_query: dict[str, Any] | None = None,
        extra_body: dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceAccountToken:
        """POST /identities/{identity_id}/service_account_tokens.

        Issue an Identity SAT using the explicit SA Key, with no automatic retries.
        ttl_seconds is 1-43200; omission uses the issuer's default.
        """
        path = path_template("/identities/{identity_id}/service_account_tokens", identity_id=identity_id)
        options = make_request_options(
            body={"ttl_seconds": ttl_seconds, "metadata": metadata},
            query={},
            headers={},
            extra_headers=sa_key_headers(sa_key, extra_headers),
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        options["max_retries"] = 0
        return self._client.request("POST", path, cast_to=ServiceAccountToken, options=options)


class AsyncServiceAccountTokens(AsyncAPIResource):
    async def create(
        self,
        identity_id: str,
        *,
        sa_key: str,
        ttl_seconds: int | NotGiven = NOT_GIVEN,
        metadata: dict[str, Any] | NotGiven = NOT_GIVEN,
        extra_headers: dict[str, str] | None = None,
        extra_query: dict[str, Any] | None = None,
        extra_body: dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceAccountToken:
        """POST /identities/{identity_id}/service_account_tokens.

        Issue an Identity SAT using the explicit SA Key, with no automatic retries.
        ttl_seconds is 1-43200; omission uses the issuer's default.
        """
        path = path_template("/identities/{identity_id}/service_account_tokens", identity_id=identity_id)
        options = make_request_options(
            body={"ttl_seconds": ttl_seconds, "metadata": metadata},
            query={},
            headers={},
            extra_headers=sa_key_headers(sa_key, extra_headers),
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        options["max_retries"] = 0
        return await self._client.request("POST", path, cast_to=ServiceAccountToken, options=options)
