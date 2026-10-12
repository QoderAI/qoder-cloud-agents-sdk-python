from __future__ import annotations

import os

import pytest

from qca import AsyncForward, AsyncManaged, AsyncServiceAccountCredential, Forward, Managed, ServiceAccountCredential

pytestmark = pytest.mark.integration


def region_config(region):
    variable = "QODER_SA_CN_KEY" if region == "cn" else "QODER_SA_GLOBAL_KEY"
    key = os.environ.get(variable)
    assert key, f"{variable} is required"
    host = "https://api.qoder.com.cn" if region == "cn" else "https://api.qoder.com"
    return key, host


@pytest.mark.parametrize("region", ["cn", "global"])
def test_sa_sync_readonly(region):
    key, host = region_config(region)
    with ServiceAccountCredential(sa_key=key, region=region, scopes=["qca.access", "forward.access"]) as credential:
        for Client, resource, path in [(Forward, "templates", "forward"), (Managed, "agents", "cloud")]:
            options = dict(base_url=f"{host}/api/v1/{path}/", max_retries=0, timeout=30)
            with Client(**options, credential=credential) as client:
                assert isinstance(getattr(client, resource).list(limit=1).data, list)
            with Client(**options, auth_mode="sa", access_token=credential.get_token()) as client:
                assert isinstance(getattr(client, resource).list(limit=1).data, list)


@pytest.mark.parametrize("region", ["cn", "global"])
async def test_sa_async_readonly(region):
    key, host = region_config(region)
    async with AsyncServiceAccountCredential(
        sa_key=key, region=region, scopes=["qca.access", "forward.access"]
    ) as credential:
        for Client, resource, path in [(AsyncForward, "templates", "forward"), (AsyncManaged, "agents", "cloud")]:
            options = dict(base_url=f"{host}/api/v1/{path}/", max_retries=0, timeout=30)
            async with Client(**options, credential=credential) as client:
                assert isinstance((await getattr(client, resource).list(limit=1)).data, list)
            async with Client(**options, auth_mode="sa", access_token=await credential.get_token()) as client:
                assert isinstance((await getattr(client, resource).list(limit=1)).data, list)
