import os

import pytest

from qca import Forward, Managed
from tests.support.harness import Config, Run


def _live_config(mode):
    if os.environ.get("QODER_RUN_LIVE") != "1":
        pytest.skip("Set QODER_RUN_LIVE=1 to run account-backed examples")
    return Config.load(
        mode,
        env_file=os.environ.get("QODER_LIVE_ENV_FILE", ".env.live"),
        timeout=float(os.environ.get("QODER_LIVE_TIMEOUT", "300")),
    )


@pytest.fixture
def live_example(request):
    mode = request.param
    config = _live_config(mode)
    context = Run(config)
    client_type = Forward if mode == "forward" else Managed
    with client_type(**config.client_options()) as client:
        try:
            yield client, context
        finally:
            context.cleanup()


@pytest.fixture
def strict_live_client(request):
    mode = request.param
    config = _live_config(mode)
    client_type = Forward if mode == "forward" else Managed
    with client_type(**config.client_options(), _strict_response_validation=True) as client:
        yield client
