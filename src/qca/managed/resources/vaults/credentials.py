from __future__ import annotations

from typing import Any, Dict, List, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.managed.types.credential import Credential
from qca.managed.types.credential_validation import CredentialValidation
from qca.managed.types.deleted_credential import DeletedCredential
from qca.managed.types.environment_variable_create_params import EnvironmentVariableCreateParams
from qca.managed.types.environment_variable_update_params import EnvironmentVariableUpdateParams
from qca.managed.types.mcpo_auth_create_params import MCPOAuthCreateParams
from qca.managed.types.mcpo_auth_update_params import MCPOAuthUpdateParams
from qca.managed.types.static_bearer_create_params import StaticBearerCreateParams
from qca.managed.types.static_bearer_update_params import StaticBearerUpdateParams

__all__ = ["Credentials", "AsyncCredentials"]


class Credentials(SyncAPIResource):
    def create(
        self,
        vault_id: str,
        *,
        auth: Union[MCPOAuthCreateParams, StaticBearerCreateParams, EnvironmentVariableCreateParams],
        display_name: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Credential:
        """POST /vaults/{vault_id}/credentials."""
        _path = path_template("/vaults/{vault_id}/credentials", vault_id=vault_id)
        options = make_request_options(
            body={"auth": auth, "display_name": display_name, "metadata": metadata},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Credential, options=options)

    def retrieve(
        self,
        credential_id: str,
        *,
        vault_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Credential:
        """GET /vaults/{vault_id}/credentials/{credential_id}."""
        _path = path_template(
            "/vaults/{vault_id}/credentials/{credential_id}", credential_id=credential_id, vault_id=vault_id
        )
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Credential, options=options)

    def update(
        self,
        credential_id: str,
        *,
        vault_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        auth: Union[
            Union[MCPOAuthUpdateParams, StaticBearerUpdateParams, EnvironmentVariableUpdateParams], None, NotGiven
        ] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Credential:
        """POST /vaults/{vault_id}/credentials/{credential_id}. Updates authentication information or metadata."""
        _path = path_template(
            "/vaults/{vault_id}/credentials/{credential_id}", credential_id=credential_id, vault_id=vault_id
        )
        options = make_request_options(
            body={"metadata": metadata, "auth": auth},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Credential, options=options)

    def list(
        self,
        vault_id: str,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Credential]:
        """GET /vaults/{vault_id}/credentials."""
        _path = path_template("/vaults/{vault_id}/credentials", vault_id=vault_id)
        options = make_request_options(
            body={},
            query={
                "name": name,
                "before_id": before_id,
                "after_id": after_id,
                "include_archived": include_archived,
                "limit": limit,
                "page": page,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Credential, options=options, page_style="PageCursor")

    def delete(
        self,
        credential_id: str,
        *,
        vault_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedCredential:
        """DELETE /vaults/{vault_id}/credentials/{credential_id}."""
        _path = path_template(
            "/vaults/{vault_id}/credentials/{credential_id}", credential_id=credential_id, vault_id=vault_id
        )
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("DELETE", _path, cast_to=DeletedCredential, options=options)

    def archive(
        self,
        credential_id: str,
        *,
        vault_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Credential:
        """POST /vaults/{vault_id}/credentials/{credential_id}/archive."""
        _path = path_template(
            "/vaults/{vault_id}/credentials/{credential_id}/archive", credential_id=credential_id, vault_id=vault_id
        )
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Credential, options=options)

    def mcp_oauth_validate(
        self,
        credential_id: str,
        *,
        vault_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CredentialValidation:
        """POST /vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate."""
        _path = path_template(
            "/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate",
            credential_id=credential_id,
            vault_id=vault_id,
        )
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=CredentialValidation, options=options)


class AsyncCredentials(AsyncAPIResource):
    async def create(
        self,
        vault_id: str,
        *,
        auth: Union[MCPOAuthCreateParams, StaticBearerCreateParams, EnvironmentVariableCreateParams],
        display_name: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Credential:
        """POST /vaults/{vault_id}/credentials."""
        _path = path_template("/vaults/{vault_id}/credentials", vault_id=vault_id)
        options = make_request_options(
            body={"auth": auth, "display_name": display_name, "metadata": metadata},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Credential, options=options)

    async def retrieve(
        self,
        credential_id: str,
        *,
        vault_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Credential:
        """GET /vaults/{vault_id}/credentials/{credential_id}."""
        _path = path_template(
            "/vaults/{vault_id}/credentials/{credential_id}", credential_id=credential_id, vault_id=vault_id
        )
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=Credential, options=options)

    async def update(
        self,
        credential_id: str,
        *,
        vault_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        auth: Union[
            Union[MCPOAuthUpdateParams, StaticBearerUpdateParams, EnvironmentVariableUpdateParams], None, NotGiven
        ] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Credential:
        """POST /vaults/{vault_id}/credentials/{credential_id}. Updates authentication information or metadata."""
        _path = path_template(
            "/vaults/{vault_id}/credentials/{credential_id}", credential_id=credential_id, vault_id=vault_id
        )
        options = make_request_options(
            body={"metadata": metadata, "auth": auth},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Credential, options=options)

    def list(
        self,
        vault_id: str,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Credential]:
        """GET /vaults/{vault_id}/credentials."""
        _path = path_template("/vaults/{vault_id}/credentials", vault_id=vault_id)
        options = make_request_options(
            body={},
            query={
                "name": name,
                "before_id": before_id,
                "after_id": after_id,
                "include_archived": include_archived,
                "limit": limit,
                "page": page,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=Credential, options=options, page_style="PageCursor")
        )

    async def delete(
        self,
        credential_id: str,
        *,
        vault_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedCredential:
        """DELETE /vaults/{vault_id}/credentials/{credential_id}."""
        _path = path_template(
            "/vaults/{vault_id}/credentials/{credential_id}", credential_id=credential_id, vault_id=vault_id
        )
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("DELETE", _path, cast_to=DeletedCredential, options=options)

    async def archive(
        self,
        credential_id: str,
        *,
        vault_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Credential:
        """POST /vaults/{vault_id}/credentials/{credential_id}/archive."""
        _path = path_template(
            "/vaults/{vault_id}/credentials/{credential_id}/archive", credential_id=credential_id, vault_id=vault_id
        )
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Credential, options=options)

    async def mcp_oauth_validate(
        self,
        credential_id: str,
        *,
        vault_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CredentialValidation:
        """POST /vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate."""
        _path = path_template(
            "/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate",
            credential_id=credential_id,
            vault_id=vault_id,
        )
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=CredentialValidation, options=options)
