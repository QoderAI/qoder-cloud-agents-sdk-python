"""运行单个场景或依次运行所有 Forward 场景。"""

from examples.common.live import run_cli
from qca import Forward

from .batch import run as batch
from .memory import run as memory
from .models import run as models
from .resources import run as resources
from .schedule import run as schedule
from .session import run as session

SCENARIOS = {
    "models": models,
    "session": session,
    "resources": resources,
    "memory": memory,
    "schedule": schedule,
    "batch": batch,
}


if __name__ == "__main__":
    run_cli("forward", Forward, SCENARIOS)
