from __future__ import annotations

from typing import Any, Dict, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.types.vault_credential import VaultCredential

__all__ = ["Credentials", "AsyncCredentials"]


class Credentials(SyncAPIResource):
    def list(
        self,
        vault_id: str,
        *,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[VaultCredential]:
        """GET /vaults/{vault_id}/credentials."""
        _path = path_template("/vaults/{vault_id}/credentials", vault_id=vault_id)
        options = make_request_options(
            body={},
            query={"limit": limit, "page": page, "after_id": after_id, "before_id": before_id, "name": name},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=VaultCredential, options=options, page_style="PageCursor")

    def create(
        self,
        vault_id: str,
        *,
        auth: Dict[str, Any],
        display_name: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VaultCredential:
        """POST /vaults/{vault_id}/credentials."""
        _path = path_template("/vaults/{vault_id}/credentials", vault_id=vault_id)
        options = make_request_options(
            body={"auth": auth, "display_name": display_name, "metadata": metadata},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=VaultCredential, options=options)

    def retrieve(
        self,
        credential_id: str,
        *,
        vault_id: str,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VaultCredential:
        """GET /vaults/{vault_id}/credentials/{credential_id}."""
        _path = path_template(
            "/vaults/{vault_id}/credentials/{credential_id}", credential_id=credential_id, vault_id=vault_id
        )
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=VaultCredential, options=options)

    def delete(
        self,
        credential_id: str,
        *,
        vault_id: str,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """DELETE /vaults/{vault_id}/credentials/{credential_id}."""
        _path = path_template(
            "/vaults/{vault_id}/credentials/{credential_id}", credential_id=credential_id, vault_id=vault_id
        )
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("DELETE", _path, cast_to=None, options=options)


class AsyncCredentials(AsyncAPIResource):
    def list(
        self,
        vault_id: str,
        *,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[VaultCredential]:
        """GET /vaults/{vault_id}/credentials."""
        _path = path_template("/vaults/{vault_id}/credentials", vault_id=vault_id)
        options = make_request_options(
            body={},
            query={"limit": limit, "page": page, "after_id": after_id, "before_id": before_id, "name": name},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request(
                "GET", _path, cast_to=VaultCredential, options=options, page_style="PageCursor"
            )
        )

    async def create(
        self,
        vault_id: str,
        *,
        auth: Dict[str, Any],
        display_name: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VaultCredential:
        """POST /vaults/{vault_id}/credentials."""
        _path = path_template("/vaults/{vault_id}/credentials", vault_id=vault_id)
        options = make_request_options(
            body={"auth": auth, "display_name": display_name, "metadata": metadata},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=VaultCredential, options=options)

    async def retrieve(
        self,
        credential_id: str,
        *,
        vault_id: str,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VaultCredential:
        """GET /vaults/{vault_id}/credentials/{credential_id}."""
        _path = path_template(
            "/vaults/{vault_id}/credentials/{credential_id}", credential_id=credential_id, vault_id=vault_id
        )
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=VaultCredential, options=options)

    async def delete(
        self,
        credential_id: str,
        *,
        vault_id: str,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """DELETE /vaults/{vault_id}/credentials/{credential_id}."""
        _path = path_template(
            "/vaults/{vault_id}/credentials/{credential_id}", credential_id=credential_id, vault_id=vault_id
        )
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("DELETE", _path, cast_to=None, options=options)
