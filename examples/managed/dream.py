"""整理 Memory Store 中的记忆，读取并打印整理后的输出。

运行：python -m examples.managed.dream
"""

from __future__ import annotations

from examples.common.live import Run, choose_model, name, run_cli
from qca import Managed

from ._cleanup import finish_session


def run(client: Managed, context: Run) -> None:
    model = choose_model(client.models.list(), context.config.model)
    context.output("selected_model", model)
    store = client.memory_stores.create(name=name("dream-input"))
    context.track("input_memory_store", store.id, lambda: client.memory_stores.delete(store.id))
    client.memory_stores.memories.create(
        store.id,
        path="sdk-example/source.md",
        content="Permanent project verification code: QODER-DREAM-SAMPLE. Preserve this exact code during consolidation.",
    )
    dream = client.dreams.create(
        inputs=[{"type": "memory_store", "memory_store_id": store.id}],
        model=model,
        instructions="Consolidate supplied memory into sdk-example/consolidated.md. Preserve the exact project verification code. Keep the original source.",
    )
    dream_id = dream.id
    context.track("dream", dream_id, lambda: finish_dream(client, context, dream_id, store.id))
    while dream.status in ("pending", "running"):
        context.pause()
        dream = client.dreams.retrieve(dream_id)
    context.output("dream_status", dream.status)
    for output in dream.outputs or []:
        for memory in client.memory_stores.memories.list(output.memory_store_id):
            if memory.path == "sdk-example/consolidated.md":
                saved = client.memory_stores.memories.retrieve(memory.id, memory_store_id=output.memory_store_id)
                context.output("output_memory_store_id", output.memory_store_id)
                context.output("memory_path", saved.path)
                context.output("memory_content", saved.content)


def finish_dream(client: Managed, context: Run, dream_id: str, input_store_id: str) -> None:
    dream = client.dreams.retrieve(dream_id)
    if dream.status in ("pending", "running"):
        client.dreams.cancel(dream_id)
        while dream.status in ("pending", "running"):
            context.pause()
            dream = client.dreams.retrieve(dream_id)
    errors = []
    actions = []
    if dream.session_id:
        actions.append(lambda: finish_session(client, context, dream.session_id))
    seen = {input_store_id}
    for output in dream.outputs or []:
        if output.memory_store_id and output.memory_store_id not in seen:
            seen.add(output.memory_store_id)
            actions.append(lambda store_id=output.memory_store_id: client.memory_stores.delete(store_id))
    actions.append(lambda: client.dreams.archive(dream_id))
    for action in actions:
        try:
            action()
        except Exception as error:
            errors.append(error)
    if errors:
        raise RuntimeError(f"Dream cleanup had {len(errors)} failures") from errors[0]


if __name__ == "__main__":
    run_cli("managed", Managed, {"dream": run})
