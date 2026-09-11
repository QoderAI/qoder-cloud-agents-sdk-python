"""上传 JSONL 批量任务，等待完成并核对任务、输出与会话回复。

运行：python -m examples.forward.batch
"""

from __future__ import annotations

import json
from typing import Any

import httpx

from examples.common.live import Run, choose_model, marker, name, run_cli, wait_reply
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

    expected, custom_id = marker(), name("task")
    data = {
        "custom_id": custom_id,
        "template_id": template_id,
        "identity_id": identity_id,
        "body": {"input": "Reply with exactly " + expected},
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
        if not current.output_file_id:
            if current.request_counts and current.request_counts.total == 0:
                return
            raise AssertionError("Batch has no output for session cleanup")
        rows = batch_rows(client, batch.id)
        if (
            len(rows) != 1
            or rows[0].get("custom_id") != custom_id
            or rows[0].get("identity_id") != identity_id
            or rows[0].get("template_id") != template_id
        ):
            raise AssertionError("Batch cleanup output does not match this run")
        if rows[0].get("session_id"):
            finish_session(client, context, rows[0]["session_id"])

    context.track("batch", batch.id, cleanup_batch)
    while batch.status not in terminal:
        context.pause()
        batch = client.batches.retrieve(batch.id)
    if (
        batch.status != "completed"
        or not batch.request_counts
        or batch.request_counts.completed != 1
        or batch.request_counts.failed != 0
        or not batch.output_file_id
    ):
        raise AssertionError("Batch did not complete exactly one successful task")
    tasks = client.batches.tasks.list(batch.id)
    if len(tasks.data) != 1 or tasks.data[0].custom_id != custom_id:
        raise AssertionError("Batch task did not round trip")
    rows = batch_rows(client, batch.id)
    if len(rows) != 1:
        raise AssertionError("Expected one Batch output row")
    row = rows[0]
    context.output("batch_output", row)
    if (
        row.get("custom_id") != custom_id
        or row.get("identity_id") != identity_id
        or row.get("template_id") != template_id
        or row.get("status") != "completed"
        or row.get("error")
        or not row.get("session_id")
    ):
        raise AssertionError("Batch output ownership or status mismatch")
    if expected not in json.dumps(row.get("response")):
        raise AssertionError("Batch response does not contain expected output")
    wait_reply(client.sessions.events, context, row["session_id"]).verify([expected])


def batch_rows(client: Forward, batch_id: str) -> list[dict[str, Any]]:
    link = client.batches.retrieve_output(batch_id)
    url = httpx.URL(link.url)
    if url.scheme not in ("http", "https") or not url.host or url.userinfo:
        raise AssertionError("Invalid Batch output URL")
    # A separate HTTP client prevents API credentials from reaching storage.
    with httpx.Client(timeout=30, follow_redirects=True) as download:
        with download.stream("GET", url) as response:
            response.raise_for_status()
            content = bytearray()
            for chunk in response.iter_bytes():
                content.extend(chunk)
                if len(content) > 4 * 1024 * 1024:
                    raise AssertionError("Batch output exceeds the example's 4 MiB limit")
    return [json.loads(line) for line in content.splitlines() if line.strip()]


if __name__ == "__main__":
    run_cli("forward", Forward, {"batch": run})
