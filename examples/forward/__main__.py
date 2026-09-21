"""运行单个场景或依次运行所有 Forward 场景。"""

from examples.common.live import run_cli
from qca import Forward

from .batch import run as batch
from .conversation import run as conversation
from .identity_config import run as identity_config
from .memory import run as memory
from .models import run as models
from .resources import run as resources
from .schedule import run as schedule
from .session import run as session
from .streaming_deltas import run as streaming_deltas

SCENARIOS = {
    "models": models,
    "session": session,
    "conversation": conversation,
    "resources": resources,
    "identity_config": identity_config,
    "memory": memory,
    "schedule": schedule,
    "batch": batch,
    "streaming_deltas": streaming_deltas,
}


if __name__ == "__main__":
    run_cli("forward", Forward, SCENARIOS)
