import httpx
import pytest

from qca import AsyncForward, AsyncManaged, Forward, Managed


@pytest.mark.parametrize("backward", [False, True])
def test_id_pagination_keeps_filters_and_direction(backward):
    requests = []

    def handle(request):
        requests.append(request)
        index = len(requests)
        assert request.url.params["name"] == "filter"
        if index == 2:
            assert request.url.params["before_id" if backward else "after_id"] == ("first" if backward else "last")
            assert ("after_id" if backward else "before_id") not in request.url.params
        return httpx.Response(
            200, json={"data": [{"id": str(index)}], "has_more": index == 1, "first_id": "first", "last_id": "last"}
        )

    with Forward(http_client=httpx.Client(transport=httpx.MockTransport(handle))) as client:
        args = {"extra_query": {"name": "filter"}, **({"before_id": "start"} if backward else {})}
        page = client.templates.list(**args)
        assert [item.id for item in page] == ["1", "2"]
        assert [item.id for item in page.data] == ["1"]


def test_page_cursor_clears_old_cursors_and_handles_empty_page():
    requests = []

    def handle(request):
        requests.append(request)
        if len(requests) == 1:
            return httpx.Response(200, json={"data": [], "next_page": "next", "has_more": True})
        assert request.url.params["page"] == "next"
        assert "after_id" not in request.url.params
        return httpx.Response(200, json={"data": [{"id": "two"}], "has_more": False})

    with Managed(
        default_query={"after_id": "old"}, http_client=httpx.Client(transport=httpx.MockTransport(handle))
    ) as client:
        assert [item.id for item in client.agents.list()] == ["two"]


def test_repeated_pagination_cursor_raises_instead_of_looping():
    with Managed(
        http_client=httpx.Client(
            transport=httpx.MockTransport(
                lambda _: httpx.Response(200, json={"data": [{"id": "one"}], "next_page": "same", "has_more": True})
            )
        )
    ) as client:
        with pytest.raises(RuntimeError, match="did not advance"):
            list(client.agents.list())


@pytest.mark.parametrize("cls", [AsyncManaged, AsyncForward])
async def test_async_list_can_be_awaited_or_iterated(cls):
    calls = []

    def handle(request):
        calls.append(request)
        cursor = request.url.params.get("page") or request.url.params.get("after_id")
        return httpx.Response(
            200,
            json={
                "data": [{"id": "two" if cursor else "one"}],
                "next_page": None if cursor else "next",
                "last_id": "one",
                "has_more": not cursor,
            },
        )

    async with cls(http_client=httpx.AsyncClient(transport=httpx.MockTransport(handle))) as client:
        resource = client.agents if cls is AsyncManaged else client.templates
        page = await resource.list()
        assert page.data[0].id == "one"
        assert [item.id async for item in resource.list()] == ["one", "two"]
        assert [item.id async for item in page] == ["one", "two"]


def test_page_from_raw_response_can_fetch_normal_followup_pages():
    def handle(request):
        more = "after_id" not in request.url.params
        return httpx.Response(
            200, json={"data": [{"id": "one" if more else "two"}], "last_id": "one", "has_more": more}
        )

    with Forward(http_client=httpx.Client(transport=httpx.MockTransport(handle))) as client:
        page = client.templates.with_raw_response.list().parse()
        assert [item.id for item in page] == ["one", "two"]


def test_cursor_returning_to_an_earlier_value_raises_instead_of_looping():
    cursors = ["b", "a", "b"]

    def handle(request):
        return httpx.Response(200, json={"data": [{"id": "item"}], "next_page": cursors.pop(0), "has_more": True})

    with Managed(http_client=httpx.Client(transport=httpx.MockTransport(handle))) as client:
        with pytest.raises(RuntimeError, match="cycle detected"):
            list(client.agents.list())


def test_explicit_page_walking_reports_exhaustion():
    def handle(request):
        first = "page" not in request.url.params
        return httpx.Response(
            200, json={"data": [{"id": "one" if first else "two"}], "next_page": "next" if first else None}
        )

    with Managed(http_client=httpx.Client(transport=httpx.MockTransport(handle))) as client:
        page = client.agents.list()
        assert page.has_next_page()
        last = page.get_next_page()
        assert [item.id for item in last.data] == ["two"]
        assert not last.has_next_page()
        with pytest.raises(RuntimeError, match="No more pages"):
            last.get_next_page()
