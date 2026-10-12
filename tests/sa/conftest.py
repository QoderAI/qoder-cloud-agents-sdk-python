import os
from pathlib import Path

import pytest

from tests.sa.config import sa_environment


@pytest.fixture(scope="session", autouse=True)
def sa_live_configuration(request):
    items = [item for item in request.session.items if item.path.parent == Path(__file__).resolve().parent]
    regions = sorted({item.callspec.params["region"] for item in items})
    execution = any(item.path.name == "test_execution_live.py" for item in items)
    try:
        values = sa_environment(
            os.environ.get("QODER_LIVE_ENV_FILE", ".env.live"), os.environ, regions, execution=execution
        )
    except ValueError as error:
        pytest.fail(str(error), pytrace=False)
    with pytest.MonkeyPatch.context() as patch:
        for key, value in values.items():
            if key.startswith("QODER_SA_"):
                patch.setenv(key, value)
        yield
