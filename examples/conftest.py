import os

import pytest

from examples.common.live import Config, Run
from qca import Forward, Managed


@pytest.fixture
def live_example(request):
    if os.environ.get("QODER_RUN_LIVE") != "1":
        pytest.skip("Set QODER_RUN_LIVE=1 to run account-backed examples")
    mode = request.param
    config = Config.load(
        mode,
        env_file=os.environ.get("QODER_LIVE_ENV_FILE", ".env.live"),
        timeout=float(os.environ.get("QODER_LIVE_TIMEOUT", "300")),
    )
    context = Run(config)
    client_type = Forward if mode == "forward" else Managed
    with client_type(**config.client_options()) as client:
        try:
            yield client, context
        finally:
            context.cleanup()
