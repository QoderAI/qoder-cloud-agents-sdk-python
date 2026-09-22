"""上传 JSONL 批量任务，等待完成并打印任务状态与输出。

运行：python -m examples.forward.batch
"""

from __future__ import annotations

import json
from typing import Any

import httpx

from examples.common.live import Run, choose_model, name, run_cli
from qca import Forward

from ._cleanup import finish_session


def run(client: Forward, context: Run) -> None:
    environment = client.environments.create(name=name("env"), config={"type": "cloud"})
    environment_id = context.track("environment", environment.id, lambda: client.environments.archive(environment.id))

    identity = client.identities.create(external_id=name("identity"), name="SDK 示例用户")
    identity_id = context.track("identity", identity.id, lambda: client.identities.delete(identity.id))

    model = choose_model(client.models.list(), context.config.model)
    context.output("selected_model", model)
    template = client.templates.create(
        name=name("template"),
        environment_id=environment_id,
        model=model,
        system="你是一个 SDK 示例助手。必要时调用工具，只使用可实际读取的数据回答问题。",
        tools=[{"type": "agent_toolset_20260401"}],
    )
    template_id = context.track("template", template.id, lambda: client.templates.archive(template.id))

    custom_id = name("task")
    data = {
        "custom_id": custom_id,
        "template_id": template_id,
        "identity_id": identity_id,
        "body": {"input": "请用一句话打个招呼。"},
    }
    input_file = client.files.upload(
        file=("input.jsonl", (json.dumps(data) + "\n").encode()), purpose="session_resource"
    )
    context.track("input_file", input_file.id, lambda: client.files.delete(input_file.id))
    batch = client.batches.create(
        input_file_id=input_file.id,
        completion_window="24h",
        idempotency_key=name("batch"),
        extra_body={"ignore_idle_window": True},
    )
    terminal = {"completed", "failed", "cancelled", "expired"}

    def cleanup_batch() -> None:
        current = client.batches.retrieve(batch.id)
        if current.status not in terminal:
            client.batches.cancel(batch.id)
        while current.status not in terminal:
            context.pause()
            current = client.batches.retrieve(batch.id)
        if current.output_file_id:
            for row in batch_rows(client, batch.id):
                if row.get("session_id"):
                    finish_session(client, context, row["session_id"])

    context.track("batch", batch.id, cleanup_batch)
    while batch.status not in terminal:
        context.pause()
        batch = client.batches.retrieve(batch.id)
    context.output("batch_status", batch.status)
    if batch.request_counts:
        context.output(
            "request_counts",
            {"completed": batch.request_counts.completed, "failed": batch.request_counts.failed},
        )
    tasks = client.batches.tasks.list(batch.id)
    context.output("tasks", [task.custom_id for task in tasks.data])
    if batch.output_file_id:
        context.output("batch_output", batch_rows(client, batch.id))


def batch_rows(client: Forward, batch_id: str) -> list[dict[str, Any]]:
    link = client.batches.retrieve_output(batch_id)
    url = httpx.URL(link.url)
    if url.scheme not in ("http", "https") or not url.host or url.userinfo:
        raise RuntimeError("Invalid Batch output URL")
    # A separate HTTP client prevents API credentials from reaching storage.
    with httpx.Client(timeout=30, follow_redirects=True) as download:
        with download.stream("GET", url) as response:
            response.raise_for_status()
            content = bytearray()
            for chunk in response.iter_bytes():
                content.extend(chunk)
                if len(content) > 4 * 1024 * 1024:
                    raise RuntimeError("Batch output exceeds the example's 4 MiB limit")
    return [json.loads(line) for line in content.splitlines() if line.strip()]


if __name__ == "__main__":
    run_cli("forward", Forward, {"batch": run})
