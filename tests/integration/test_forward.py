import pytest

from tests.support.assertions import assert_readonly_list_response
from tests.support.scenarios.forward import SCENARIOS

pytestmark = pytest.mark.integration


@pytest.mark.parametrize("live_example", ["forward"], indirect=True)
@pytest.mark.parametrize("scenario", SCENARIOS.values(), ids=SCENARIOS)
def test_forward_example(live_example, scenario):
    client, context = live_example
    scenario(client, context)


@pytest.mark.parametrize("strict_live_client", ["forward"], indirect=True)
@pytest.mark.parametrize("resource", ["models", "templates", "sessions"])
def test_forward_strict_response_contract(strict_live_client, resource):
    assert_readonly_list_response(strict_live_client, resource)
