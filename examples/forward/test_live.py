import pytest

from .__main__ import SCENARIOS

pytestmark = pytest.mark.live


@pytest.mark.parametrize("live_example", ["forward"], indirect=True)
@pytest.mark.parametrize("scenario", SCENARIOS.values(), ids=SCENARIOS)
def test_forward_example(live_example, scenario):
    client, context = live_example
    scenario(client, context)
