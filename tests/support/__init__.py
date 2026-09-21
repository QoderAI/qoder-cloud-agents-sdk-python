"""tests 自足支持层：断言层 + 运行时基元副本 + verbatim 场景 + HTTP 桩 + 清理。

tests 不依赖 examples、examples 亦不依赖 tests（双向断开）。场景 SCENARIOS 请从
tests.support.scenarios.forward / tests.support.scenarios.managed 取用。
"""

from tests.support.assertions import TurnResult, turn, wait_reply
from tests.support.cleanup import finish_dream, finish_session_forward, finish_session_managed
from tests.support.harness import Config, Run, choose_model, marker, name, read_env, safe_error
from tests.support.memory import ProjectMemory
from tests.support.stub import ExampleService

__all__ = [
    "Config",
    "ExampleService",
    "ProjectMemory",
    "Run",
    "TurnResult",
    "choose_model",
    "finish_dream",
    "finish_session_forward",
    "finish_session_managed",
    "marker",
    "name",
    "read_env",
    "safe_error",
    "turn",
    "wait_reply",
]
