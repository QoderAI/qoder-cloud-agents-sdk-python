"""Read-only Search checks; no resource creation or model execution."""

import json
from pathlib import Path
from uuid import uuid4

import pytest

from qca import APIError
from tests.support.harness import safe_error

CASES = json.loads((Path(__file__).parents[1] / "fixtures/search-contracts.json").read_text())["cases"]
pytestmark = pytest.mark.integration


@pytest.mark.parametrize(
    "strict_live_client,resource",
    [(case["mode"], case["resource"]) for case in CASES],
    indirect=["strict_live_client"],
)
def test_search_readonly(strict_live_client, resource, record_property):
    try:
        api = getattr(strict_live_client, resource)
        raw = api.with_raw_response.search(limit=1)
        page = raw.parse()
        record_property("request_id", raw.headers.get("x-request-id", ""))
        record_property("first_page_items", len(page.data))
        assert len(page.data) <= 1 and isinstance(page.has_more, bool)
        assert all(item.id for item in page.data)
        if page.has_next_page():
            next_page = page.get_next_page()
            record_property("second_page_items", len(next_page.data))
            assert len(next_page.data) <= 1 and all(item.id for item in next_page.data)
        empty = api.search(limit=1, metadata={"sdk_search_probe": uuid4().hex})
        assert empty.data == [] and not empty.has_next_page()
    except APIError as error:
        pytest.fail(safe_error(error), pytrace=False)
