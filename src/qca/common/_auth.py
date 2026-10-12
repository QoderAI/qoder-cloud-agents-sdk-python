from __future__ import annotations

import os
from typing import Literal

from .credentials import AsyncCredential, Credential
from .service_account import AsyncServiceAccountCredential, ServiceAccountCredential

AuthMode = Literal["pat", "sa"]


def resolve_auth(
    *,
    pat: str | None,
    access_token: str | None,
    auth_mode: AuthMode | None,
    credential: Credential | AsyncCredential | None,
    is_async: bool,
) -> tuple[AuthMode, str | None]:
    native_sa = isinstance(credential, (ServiceAccountCredential, AsyncServiceAccountCredential))
    mode = auth_mode if auth_mode is not None else ("sa" if native_sa else "pat")
    if mode not in ("pat", "sa"):
        raise ValueError("auth_mode must be pat or sa")
    if native_sa and (mode != "sa" or pat is not None or access_token is not None):
        raise ValueError("ServiceAccountCredential requires SA mode without a static token")
    if mode == "sa" and pat is not None:
        raise ValueError("pat cannot be used in SA mode")
    if access_token is not None and (pat is not None or credential is not None):
        raise ValueError("access_token cannot be combined with pat or credential")
    if isinstance(credential, ServiceAccountCredential) and is_async:
        raise TypeError("Use AsyncServiceAccountCredential with an asynchronous client")
    if isinstance(credential, AsyncServiceAccountCredential) and not is_async:
        raise TypeError("Use ServiceAccountCredential with a synchronous client")
    for value in (pat, access_token):
        if value is not None and (not isinstance(value, str) or not value.strip()):
            raise ValueError("Configured access token must not be empty")
    # Preserve explicit PAT + custom Credential precedence, but not ambient PAT masking.
    token = access_token if access_token is not None else pat
    if token is None and credential is None:
        token = os.environ.get("QODER_ACCESS_TOKEN") or (os.environ.get("QODER_PAT") if mode == "pat" else None)
    return mode, token
