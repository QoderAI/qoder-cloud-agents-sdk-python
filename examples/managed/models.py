"""查询账号启用的模型，并选择一个可用模型。

运行：python -m examples.managed.models
"""

from __future__ import annotations

from examples.common.live import Run, choose_model, run_cli
from qca import Managed


def run(client: Managed, context: Run) -> None:
    models = client.models.list()
    context.output("models", [{"id": model.id, "is_enabled": model.is_enabled} for model in models.data])
    context.output("selected_model", choose_model(models, context.config.model))


if __name__ == "__main__":
    run_cli("managed", Managed, {"models": run})
