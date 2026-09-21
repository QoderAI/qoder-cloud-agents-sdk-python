"""运行单个场景或依次运行所有 Managed 场景。"""

from examples.common.live import run_cli
from qca import Managed

from .conversation import run as conversation
from .custom_tools import run as custom_tools
from .deployment import run as deployment
from .dream import run as dream
from .memory import run as memory
from .models import run as models
from .resources import run as resources
from .session import run as session
from .streaming_deltas import run as streaming_deltas

SCENARIOS = {
    "models": models,
    "session": session,
    "conversation": conversation,
    "resources": resources,
    "custom_tools": custom_tools,
    "memory": memory,
    "deployment": deployment,
    "dream": dream,
    "streaming_deltas": streaming_deltas,
}


if __name__ == "__main__":
    run_cli("managed", Managed, SCENARIOS)
