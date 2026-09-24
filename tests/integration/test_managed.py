import pytest

from tests.support.assertions import assert_readonly_list_response
from tests.support.scenarios.managed import SCENARIOS

pytestmark = pytest.mark.integration


@pytest.mark.parametrize("live_example", ["managed"], indirect=True)
@pytest.mark.parametrize("scenario", SCENARIOS.values(), ids=SCENARIOS)
def test_managed_example(live_example, scenario):
    client, context = live_example
    scenario(client, context)


@pytest.mark.parametrize("strict_live_client", ["managed"], indirect=True)
@pytest.mark.parametrize("resource", ["models", "agents", "sessions"])
def test_managed_strict_response_contract(strict_live_client, resource):
    assert_readonly_list_response(strict_live_client, resource)
