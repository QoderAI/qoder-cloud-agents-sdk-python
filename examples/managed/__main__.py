"""运行单个场景或依次运行所有 Managed 场景。"""

from examples.common.live import run_cli
from qca import Managed

from .deployment import run as deployment
from .dream import run as dream
from .memory import run as memory
from .models import run as models
from .resources import run as resources
from .session import run as session

SCENARIOS = {
    "models": models,
    "session": session,
    "resources": resources,
    "memory": memory,
    "deployment": deployment,
    "dream": dream,
}


if __name__ == "__main__":
    run_cli("managed", Managed, SCENARIOS)
