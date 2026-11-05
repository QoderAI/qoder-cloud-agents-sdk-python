import inspect
import json

import httpx
import pytest

from qca import AsyncForward, AsyncManaged, Forward, Managed


async def resolve(value):
    return await value if inspect.isawaitable(value) else value


@pytest.mark.parametrize("async_", [False, True])
async def test_byoc_tunnel_binding(async_):
    requests = []

    def handle(request):
        body = json.loads(request.content)
        requests.append(body)
        response = {"id": "test"}
        if body.get("tunnel_id"):
            response["tunnel_id"] = body["tunnel_id"]
        return httpx.Response(200, json=response)

    http = httpx.AsyncClient if async_ else httpx.Client
    forward = (AsyncForward if async_ else Forward)(pat="test", http_client=http(transport=httpx.MockTransport(handle)))
    managed = (AsyncManaged if async_ else Managed)(pat="test", http_client=http(transport=httpx.MockTransport(handle)))
    try:
        for binding in ({}, {"tunnel_id": "tnl_test"}):
            await resolve(managed.sessions.create(agent="agent_test", environment_id="env_test", **binding))
            assert requests[-1] == {
                "agent": "agent_test",
                "environment_id": "env_test",
                "metadata": requests[-1]["metadata"],
                **binding,
            }
            template = await resolve(
                forward.templates.create(name="demo", model="auto", environment_id="env_test", **binding)
            )
            assert requests[-1] == {"name": "demo", "model": "auto", "environment_id": "env_test", **binding}
            assert template.tunnel_id == binding.get("tunnel_id")
            assert "tunnel_id" in type(template).model_fields
            deployment_params = {
                "name": "demo",
                "agent": "agent_test",
                "environment_id": "env_test",
                "initial_events": [{"type": "user.message", "content": [{"type": "text", "text": "hello"}]}],
                **binding,
            }
            deployment = await resolve(managed.deployments.create(**deployment_params))
            assert requests[-1] == deployment_params
            assert deployment.tunnel_id == binding.get("tunnel_id")
            assert "tunnel_id" in type(deployment).model_fields
        for patch in ({}, {"tunnel_id": "tnl_other"}, {"tunnel_id": None}):
            await resolve(forward.templates.update("tmpl_test", **patch))
            assert requests[-1] == patch
            await resolve(managed.deployments.update("dep_test", **patch))
            assert requests[-1] == patch
    finally:
        await resolve(managed.close())
        await resolve(forward.close())
