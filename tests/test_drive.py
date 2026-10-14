"""Drive wire behavior from the public API contract, for both client modes."""

import inspect
import json

import httpx
import pytest

from qca import AsyncForward, Forward, InternalServerError


async def resolve(value):
    return await value if inspect.isawaitable(value) else value


@pytest.mark.parametrize("async_", [False, True])
async def test_drive_paths_pages_and_typed_metadata(async_):
    requests = []
    cursor = "opaque/+%=&"

    def handler(request):
        requests.append(request)
        assert request.headers["authorization"] == "Bearer test-sat"
        assert request.url.params["identity_id"] == "idn_test"
        assert request.url.params["path"] == "目录/a b+~*"
        assert b"path=%E7%9B%AE%E5%BD%95/a+b%2B~%2A" in request.url.query
        assert b"extra=a%2Fb" in request.url.query
        if len(requests) == 1:
            return httpx.Response(
                200,
                json={
                    "entries": [
                        {"path": "a.txt", "name": "a.txt", "type": "file", "size": 0},
                        {"path": "a", "name": "a", "type": "directory"},
                    ],
                    "next_page_token": cursor,
                },
            )
        assert request.url.params["page_token"] == cursor
        return httpx.Response(200, json={"entries": []})

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handler))
    client = (AsyncForward if async_ else Forward)(
        auth_mode="sa",
        access_token="test-sat",
        http_client=http,
        default_query={"extra": "a/b", "path": "replaced"},
        _strict_response_validation=True,
    )
    try:
        first = await resolve(
            client.drives.list_entries(
                identity_id="idn_test", path="replaced-again", extra_query={"path": "目录/a b+~*"}
            )
        )
        assert [entry.path for entry in first.entries] == ["a.txt", "a"]
        assert first.entries[0].size == 0
        assert first.entries[1].size is None
        last = await resolve(
            client.drives.list_entries(identity_id="idn_test", path="目录/a b+~*", page_token=first.next_page_token)
        )
        assert last.entries == [] and last.next_page_token is None
    finally:
        await resolve(client.close())


@pytest.mark.parametrize("async_", [False, True])
async def test_drive_mutation_bodies_signed_headers_and_partial_error(async_):
    requests = []

    def handler(request):
        requests.append(request)
        assert request.url.params.multi_items() == [("identity_id", "idn_test")]
        route = request.url.path.rsplit("/", 1)[-1]
        if route.endswith("-url"):
            assert request.method == "POST"
            assert request.headers["Idempotency-Key"] == "retry-one"
            assert json.loads(request.content) == (
                {"path": "reports/readme.txt", "content_type": "text/plain"}
                if route == "upload-url"
                else {"path": "reports/readme.txt"}
            )
            return httpx.Response(
                200,
                json={
                    "url": "https://storage.test/signed",
                    "method": "PUT" if route == "upload-url" else "GET",
                    "headers": {"Content-Type": "text/plain"},
                    "expires_at": "2026-10-14T02:15:00Z",
                },
            )
        assert request.method == "DELETE"
        if route == "entries":
            assert json.loads(request.content) == {"path": "reports", "recursive": False}
            return httpx.Response(200, json={"deleted_count": 0})
        assert request.content == b""
        return httpx.Response(
            503,
            json={
                "request_id": "req_partial",
                "error": {"code": "drive_delete_partial", "deleted_count": 7, "message": "partial"},
            },
        )

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handler))
    client = (AsyncForward if async_ else Forward)(pat="test-pat", http_client=http, max_retries=2)
    try:
        upload = await resolve(
            client.drives.create_upload_url(
                identity_id="idn_test",
                path="reports/readme.txt",
                content_type="text/plain",
                idempotency_key="retry-one",
            )
        )
        assert upload.headers == {"Content-Type": "text/plain"} and upload.method == "PUT"
        download = await resolve(
            client.drives.create_download_url(
                identity_id="idn_test", path="reports/readme.txt", idempotency_key="retry-one"
            )
        )
        assert download.method == "GET" and download.size is None
        deleted = await resolve(client.drives.delete_entry(identity_id="idn_test", path="reports", recursive=False))
        assert deleted.deleted_count == 0
        with pytest.raises(InternalServerError) as raised:
            await resolve(client.drives.clear(identity_id="idn_test"))
        assert raised.value.code == "drive_delete_partial"
        assert raised.value.request_id == "req_partial"
        assert raised.value.body["error"]["deleted_count"] == 7
        assert len(requests) == 4
    finally:
        await resolve(client.close())


@pytest.mark.parametrize("async_", [False, True])
async def test_template_managed_tools_preserves_omission_null_and_empty(async_):
    bodies = []

    def handler(request):
        bodies.append(json.loads(request.content))
        return httpx.Response(200, json={"managed_tool_config": {"enabled_tools": ["drive", "schedule"]}})

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handler))
    client = (AsyncForward if async_ else Forward)(pat="test-pat", http_client=http)
    try:
        await resolve(client.templates.update("tmpl_test"))
        await resolve(client.templates.update("tmpl_test", managed_tool_config=None))
        await resolve(client.templates.update("tmpl_test", managed_tool_config={"enabled_tools": []}))
        result = await resolve(
            client.templates.create(
                name="drive",
                model="auto",
                environment_id="env_test",
                managed_tool_config={"enabled_tools": ["drive", "schedule"]},
            )
        )
        assert bodies[:3] == [{}, {"managed_tool_config": None}, {"managed_tool_config": {"enabled_tools": []}}]
        assert bodies[3]["managed_tool_config"] == {"enabled_tools": ["drive", "schedule"]}
        assert result.managed_tool_config.enabled_tools == ["drive", "schedule"]
    finally:
        await resolve(client.close())


@pytest.mark.parametrize("async_", [False, True])
async def test_drive_does_not_normalize_paths_or_clamp_limits(async_):
    from qca import BadRequestError

    expected = {}

    def handler(request):
        assert request.url.params["path"] == expected["path"]
        assert request.url.params["limit"] == str(expected["limit"])
        assert request.url.params.get_list("identity_id") == ["idn_test"]
        assert request.content == b""
        if expected["path"] == "" and expected["limit"] in (1, 100):
            return httpx.Response(200, json={"entries": []})
        return httpx.Response(400, json={"error": {"code": "invalid_argument", "message": "invalid Drive query"}})

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handler))
    client = (AsyncForward if async_ else Forward)(pat="test-pat", http_client=http)
    try:
        for limit in (1, 100):
            expected.update(path="", limit=limit)
            assert (
                await resolve(client.drives.list_entries(identity_id="idn_test", path="", limit=limit))
            ).entries == []
        for path, limit in [
            ("/absolute", 20),
            ("../other", 20),
            ("a\\b", 20),
            ("a%2Fb", 20),
            (" a ", 20),
            ("", 0),
            ("", 101),
        ]:
            expected.update(path=path, limit=limit)
            with pytest.raises(BadRequestError) as raised:
                await resolve(client.drives.list_entries(identity_id="idn_test", path=path, limit=limit))
            assert raised.value.code == "invalid_argument"
    finally:
        await resolve(client.close())
