import pytest

from tests.support.scenarios.forward import SCENARIOS

pytestmark = pytest.mark.integration


@pytest.mark.parametrize("live_example", ["forward"], indirect=True)
@pytest.mark.parametrize("scenario", SCENARIOS.values(), ids=SCENARIOS)
def test_forward_example(live_example, scenario):
    client, context = live_example
    scenario(client, context)
