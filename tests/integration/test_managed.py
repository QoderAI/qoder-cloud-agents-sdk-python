import pytest

from tests.support.scenarios.managed import SCENARIOS

pytestmark = pytest.mark.integration


@pytest.mark.parametrize("live_example", ["managed"], indirect=True)
@pytest.mark.parametrize("scenario", SCENARIOS.values(), ids=SCENARIOS)
def test_managed_example(live_example, scenario):
    client, context = live_example
    scenario(client, context)
