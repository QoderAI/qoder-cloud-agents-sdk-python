from __future__ import annotations

import importlib.metadata

import httpx
import pytest

import qca
from qca import (
    NOT_GIVEN,
    APIConnectionError,
    APIStatusError,
    APITimeoutError,
    AsyncForward,
    AsyncManaged,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    Forward,
    InternalServerError,
    Managed,
    NotFoundError,
    NotGiven,
    PermissionDeniedError,
    RateLimitError,
    UnprocessableEntityError,
    __version__,
)

# Fixed upstream provenance for this shared-semantics baseline:
#   repository: anthropics/anthropic-sdk-python
#   tag:        v1.7.0
#   commit:     0af0190679a9e80388bd1b0328d557c9a91a11b2
# Consistency here means offline semantics ALREADY shared by QCA and the pinned
# Anthropic baseline. It does NOT mirror Anthropic's full public surface. QCA's
# intentional differences are NOT asserted: Forward/Managed + async clients, PAT
# and Qoder headers, resumable stream, httpx, the qca-sdk/qca package + version,
# the safe-retry policy, and the server-side error envelope. Anthropic public
# APIs that QCA lacks get their own tasks; they are never shimmed, skipped, or
# xfail'd here.

SYNC_CLIENTS = [Forward, Managed]
ASYNC_CLIENTS = [AsyncForward, AsyncManaged]
ALL_CLIENTS = SYNC_CLIENTS + ASYNC_CLIENTS

PUBLIC_STATUS_ERRORS = [
    BadRequestError,
    AuthenticationError,
    PermissionDeniedError,
    NotFoundError,
    ConflictError,
    UnprocessableEntityError,
    RateLimitError,
    InternalServerError,
]


def test_top_level_clients_sentinel_version_and_exceptions_are_public():
    # (1) The four clients, the missing-argument sentinel and its type, the
    # version and the shared public exceptions are importable from qca.
    for client_cls in ALL_CLIENTS:
        assert isinstance(client_cls, type)
    assert isinstance(NOT_GIVEN, NotGiven)
    assert isinstance(__version__, str) and __version__
    for exc in [APIConnectionError, APITimeoutError, APIStatusError, *PUBLIC_STATUS_ERRORS]:
        assert isinstance(exc, type)


@pytest.mark.parametrize("exc", PUBLIC_STATUS_ERRORS)
def test_status_errors_inherit_api_status_error(exc):
    # (2) Every shared status error subclasses APIStatusError; the timeout error
    # is a connection error. We do NOT require Anthropic-only error subclasses.
    assert issubclass(exc, APIStatusError)


def test_timeout_is_a_connection_error():
    assert issubclass(APITimeoutError, APIConnectionError)


def test_not_given_is_falsy_stable_repr_and_distinct_from_none():
    # (3) NOT_GIVEN is falsy, has a stable repr, and is not None.
    assert bool(NOT_GIVEN) is False
    assert repr(NOT_GIVEN) == "NOT_GIVEN"
    assert NOT_GIVEN is not None


@pytest.mark.parametrize("client_cls", SYNC_CLIENTS)
def test_sync_client_rejects_non_httpx_client(client_cls):
    # (4) Keyword-only construction validates the injected transport type.
    with pytest.raises(TypeError, match="httpx.Client"):
        client_cls(pat="test-token", base_url="https://api.test/prefix/", http_client=object())


@pytest.mark.parametrize("client_cls", ASYNC_CLIENTS)
def test_async_client_rejects_non_async_httpx_client(client_cls):
    with pytest.raises(TypeError, match="httpx.AsyncClient"):
        client_cls(pat="test-token", base_url="https://api.test/prefix/", http_client=httpx.Client())


@pytest.mark.parametrize("client_cls", ALL_CLIENTS)
def test_client_construction_is_keyword_only(client_cls):
    with pytest.raises(TypeError):
        client_cls("positional-pat")  # type: ignore[misc]


@pytest.mark.parametrize("client_cls", SYNC_CLIENTS)
@pytest.mark.parametrize("bad", [-1, True, 1.5])
def test_invalid_max_retries_is_rejected(client_cls, bad):
    # (5) Non-negative-int guard on max_retries and absolute-HTTP(S) guard on base_url.
    with pytest.raises(ValueError, match="max_retries"):
        client_cls(
            pat="test-token",
            base_url="https://api.test/prefix/",
            http_client=httpx.Client(transport=httpx.MockTransport(lambda _: httpx.Response(200, json={}))),
            max_retries=bad,
        )


@pytest.mark.parametrize("client_cls", SYNC_CLIENTS)
@pytest.mark.parametrize(
    "bad_url",
    ["ftp://api.test/x", "https://user:pass@api.test/x", "https://api.test/x?a=1", "https://api.test/x#frag"],
)
def test_invalid_base_url_is_rejected(client_cls, bad_url):
    with pytest.raises(ValueError, match="base_url"):
        client_cls(
            pat="test-token",
            base_url=bad_url,
            http_client=httpx.Client(transport=httpx.MockTransport(lambda _: httpx.Response(200, json={}))),
        )


@pytest.mark.parametrize("client_cls", SYNC_CLIENTS)
def test_context_manager_closes_the_transport(client_cls):
    # (5) Context-manager lifecycle closes the underlying transport; is_closed()
    # is a method that reports the httpx client state.
    http = httpx.Client(transport=httpx.MockTransport(lambda _: httpx.Response(200, json={})))
    with client_cls(pat="test-token", base_url="https://api.test/prefix/", http_client=http) as client:
        assert client.is_closed() is False
    assert client.is_closed() is True


def test_version_matches_installed_metadata_or_source_fallback():
    # (6) When installed, qca.__version__ mirrors the qca-sdk distribution;
    # from an uninstalled source tree the fallback string is used.
    try:
        installed = importlib.metadata.version("qca-sdk")
    except importlib.metadata.PackageNotFoundError:
        assert __version__  # source fallback keeps a non-empty version string
    else:
        assert __version__ == installed
