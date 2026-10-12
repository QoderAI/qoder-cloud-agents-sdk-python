from functools import partial

import httpx
import pytest

from examples.common.live import Config
from qca import AsyncForward, AsyncManaged, AsyncServiceAccountCredential, Forward, Managed, ServiceAccountCredential


@pytest.fixture(autouse=True)
def clean_auth_env(monkeypatch):
    for name in (
        "QODER_AUTH_MODE",
        "QODER_SA_KEY",
        "QODER_ACCESS_TOKEN",
        "QODER_SA_REGION",
        "QODER_PAT",
        "QODER_FORWARD_PAT",
        "QODER_MANAGED_PAT",
        "QODER_FORWARD_BASE_URL",
        "QODER_MANAGED_BASE_URL",
    ):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setenv("QODER_PAT", "ambient-pat")


@pytest.mark.parametrize("mode,client_type", [("forward", Forward), ("managed", Managed)])
@pytest.mark.parametrize("auth_mode", ["pat", "sa"])
def test_examples_send_selected_token(mode, client_type, auth_mode, monkeypatch, tmp_path):
    monkeypatch.setenv("QODER_AUTH_MODE", auth_mode)
    monkeypatch.setenv("QODER_ACCESS_TOKEN", "static-sat")
    requests = []

    def respond(request):
        requests.append(request)
        return httpx.Response(200, json={"data": []})

    config = Config.load(mode, env_file=tmp_path / "missing.env")
    with config.open_client(
        partial(client_type, http_client=httpx.Client(transport=httpx.MockTransport(respond)))
    ) as client:
        client.models.list()
    assert requests[0].headers["Authorization"] == f"Bearer {'static-sat' if auth_mode == 'sa' else 'ambient-pat'}"
    assert "static-sat" not in repr(config)


@pytest.mark.parametrize("values", [{}, {"QODER_SA_KEY": "key", "QODER_ACCESS_TOKEN": "sat"}])
def test_sa_examples_fail_instead_of_falling_back_to_pat(values, monkeypatch, tmp_path):
    monkeypatch.setenv("QODER_AUTH_MODE", "sa")
    for name, value in values.items():
        monkeypatch.setenv(name, value)
    with pytest.raises(ValueError, match="exactly one"):
        Config.load("forward", env_file=tmp_path / "missing.env")


@pytest.mark.parametrize("is_async", [False, True])
@pytest.mark.parametrize(
    "mode,client_type,async_client_type", [("forward", Forward, AsyncForward), ("managed", Managed, AsyncManaged)]
)
async def test_example_key_exchange_uses_selected_region_and_closes_credential(
    is_async,
    mode,
    client_type,
    async_client_type,
    monkeypatch,
    tmp_path,
):
    monkeypatch.setenv("QODER_AUTH_MODE", "sa")
    monkeypatch.setenv("QODER_SA_KEY", "test-key")
    monkeypatch.setenv("QODER_SA_REGION", "global")
    requests = []

    def respond(request):
        requests.append(request)
        if request.url.path.endswith("/exchange"):
            return httpx.Response(
                200, json={"access_token": "exchanged-sat", "token_type": "Bearer", "expires_in": 3600}
            )
        return httpx.Response(200, json={"data": []})

    config = Config.load(mode, env_file=tmp_path / "missing.env")
    transport = httpx.MockTransport(respond)
    if is_async:
        monkeypatch.setattr(
            "examples.common.live.AsyncServiceAccountCredential",
            partial(AsyncServiceAccountCredential, http_client=httpx.AsyncClient(transport=transport)),
        )
        async with config.open_async_client(
            partial(async_client_type, http_client=httpx.AsyncClient(transport=transport))
        ) as client:
            credential = client.credential
            await client.models.list()
        with pytest.raises(RuntimeError, match="closed"):
            await credential.get_token()
    else:
        monkeypatch.setattr(
            "examples.common.live.ServiceAccountCredential",
            partial(ServiceAccountCredential, http_client=httpx.Client(transport=transport)),
        )
        with config.open_client(partial(client_type, http_client=httpx.Client(transport=transport))) as client:
            credential = client.credential
            client.models.list()
        with pytest.raises(RuntimeError, match="closed"):
            credential.get_token()
    assert [r.headers["Authorization"] for r in requests] == ["Bearer test-key", "Bearer exchanged-sat"]
    assert [r.url.host for r in requests] == ["openapi.qoder.sh", "api.qoder.com"]
