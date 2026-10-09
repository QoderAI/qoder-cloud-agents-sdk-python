import pytest

from tests.support.scenarios.api_expansion import SCENARIOS

pytestmark = pytest.mark.integration


@pytest.mark.parametrize(
    "live_example,scenario",
    list(SCENARIOS.values()),
    ids=list(SCENARIOS),
    indirect=["live_example"],
)
def test_new_api_live(live_example, scenario):
    client, context = live_example
    try:
        scenario(client, context)
    finally:
        for output in context.outputs:
            print(f"{output['label']}: {output['value']}")
