"""离线场景回放使用的 HTTP 桩（逐字迁自 tests/test_examples.py 的 ExampleService）。

ExampleService 的内部契约断言（挂载路径 / Idempotency-Key / skill 版本 /
ignore_idle_window / MEMORY.md 索引 / override op 等）保持原样；patch_batch_rows 把 batch
场景的输出下载改指桩数据，确保离线回放不发真实网络请求。
"""

from __future__ import annotations

import json
from email.parser import BytesParser
from email.policy import default

import httpx

from tests.support.scenarios import forward as forward_scenarios


class ExampleService:
    """A stateful HTTP stub: replies are derived from uploaded resources and memory."""

    def __init__(self, mode):
        self.mode = mode
        self.objects = {}
        self.contents = {}
        self.events = {}
        self.mounts = {}
        self.overrides = {}
        self.outputs = {}
        self.counter = 0
        self.deleted = []

    def create(self, kind, body):
        self.counter += 1
        item = {**body, "id": f"{kind}-{self.counter}"}
        self.objects[item["id"]] = item
        return item

    def session(self, body):
        session = self.create("session", {**body, "status": "idle"})
        self.events[session["id"]] = []
        for event in body.get("initial_events", []):
            self.send(session["id"], event)
        return session

    def send(self, session_id, event):
        session = self.objects[session_id]
        user_event = self.create("event", event)
        self.events[session_id].append(user_event)
        content = event.get("content", [])
        prompt = content if isinstance(content, str) else "".join(block.get("text", "") for block in content)
        text = prompt
        agent = self.objects[session.get("template_id") or session.get("agent")]
        if "SDK_EXAMPLE_VALUE" in prompt:
            resource = next(r for r in session["resources"] if r["type"] == "file")
            assert resource["mount_path"] == "/data/workspace/sdk-example.txt"
            text = self.contents[resource["file_id"]].decode()
            if self.mode == "forward":
                override = self.overrides[session["identity_id"], session["template_id"]]
                assert override["op"] == "set"
                text += " " + override["value"]
            else:
                text += " " + session["environment_variables"]["SDK_EXAMPLE_VALUE"]
        elif "EXAMPLE_SKILL_CODE" in prompt:
            skill = agent["skills"][0]
            text = self.contents[skill["skill_id"]].decode()
        elif "项目约定" in prompt:
            store_id = (
                self.mounts[session["identity_id"], session["template_id"]]
                if self.mode == "forward"
                else next(r["memory_store_id"] for r in session["resources"] if r["type"] == "memory_store")
            )
            text = "\n".join(item["content"] for item in self.objects.values() if item.get("store_id") == store_id)
            assert "MEMORY.md" in [
                item.get("path") for item in self.objects.values() if item.get("store_id") == store_id
            ]
        events = [
            {"type": "agent.tool_use", "name": "Read", "evaluated_permission": "allow"},
            {"type": "agent.message", "content": [{"type": "text", "text": text}]},
            {"type": "session.status_idle", "stop_reason": {"type": "end_turn"}},
        ]
        self.events[session_id].extend(self.create("event", item) for item in events)
        return user_event

    def __call__(self, request):
        path = request.url.path.split("/api/v1/", 1)[1].split("/", 1)[1]
        parts = path.split("/")
        verb = request.method
        body = {}
        if request.content:
            if request.headers.get("content-type", "").startswith("multipart/"):
                message = BytesParser(policy=default).parsebytes(
                    b"Content-Type: " + request.headers["content-type"].encode() + b"\r\n\r\n" + request.content
                )
                body = {
                    part.get_param("name", header="content-disposition"): part.get_payload(decode=True)
                    for part in message.iter_parts()
                }
            else:
                body = json.loads(request.content)

        def reply(data):
            if isinstance(data, dict) and isinstance(data.get("agent"), str):
                data = {**data, "agent": {"id": data["agent"]}}
            return httpx.Response(200, json=data)

        if path == "models":
            return reply({"data": [{"id": "ultimate", "is_enabled": True}]})
        if parts[0] == "sessions" and len(parts) >= 3:
            session_id = parts[1]
            if parts[2] == "events":
                if verb == "POST":
                    return reply({"data": [self.send(session_id, e) for e in body["events"]]})
                events = self.events[session_id]
                after = request.headers.get("Last-Event-ID") or request.url.params.get("after_id")
                if after:
                    events = events[next(i for i, e in enumerate(events) if e["id"] == after) + 1 :]
                if parts[-1] == "stream":
                    return httpx.Response(
                        200,
                        text="".join(f"id: {e['id']}\nevent: {e['type']}\ndata: {json.dumps(e)}\n\n" for e in events),
                        headers={"content-type": "text/event-stream"},
                    )
                return reply({"data": events, "has_more": False})
            if parts[2] == "resources":
                return reply({"data": self.objects[session_id]["resources"], "has_more": False})
        if parts[0] == "memory_stores" and len(parts) >= 3 and parts[2] == "memories":
            store_id = parts[1]
            if verb == "POST":
                return reply(self.create("memory", {**body, "store_id": store_id}))
            if len(parts) == 4:
                assert self.objects[parts[3]]["store_id"] == store_id
                return reply(self.objects[parts[3]])
            return reply(
                {
                    "data": [item for item in self.objects.values() if item.get("store_id") == store_id],
                    "has_more": False,
                }
            )
        if parts[0] == "identities" and len(parts) >= 5:
            identity, template = parts[1], parts[3]
            if parts[4] == "config":
                self.overrides[identity, template] = body["identity_config"]["environment_variables"][
                    "SDK_EXAMPLE_VALUE"
                ]
                return reply({})
            if parts[4] == "memory_stores":
                if verb == "POST":
                    self.mounts[identity, template] = body["memory_store_id"]
                    return reply({})
                if verb == "DELETE":
                    del self.mounts[identity, template]
                    return reply({})
                return reply({"data": [{"memory_store_id": self.mounts[identity, template]}]})
        if len(parts) == 1 and verb == "POST":
            kind = parts[0]
            if self.mode == "forward" and kind == "memory_stores":
                assert request.headers.get("Idempotency-Key"), "Idempotency-Key header is required"
            if kind in ("files", "skills"):
                item = self.create(kind, {"latest_version": "v1"} if kind == "skills" else {})
                self.contents[item["id"]] = body["file" if kind == "files" else "files"]
            elif kind in ("agents", "templates"):
                for skill in body.get("skills", []):
                    assert skill["version"] == self.objects[skill["skill_id"]]["latest_version"]
                item = self.create(kind, body)
            elif kind == "sessions":
                item = self.session(body)
            elif kind == "dreams":
                store_id = body["inputs"][0]["memory_store_id"]
                source = next(item["content"] for item in self.objects.values() if item.get("store_id") == store_id)
                output = self.create("memory_stores", {})
                self.create(
                    "memory", {"store_id": output["id"], "path": "sdk-example/consolidated.md", "content": source}
                )
                item = self.create(
                    "dream",
                    {"status": "completed", "outputs": [{"type": "memory_store", "memory_store_id": output["id"]}]},
                )
            elif kind == "batches":
                assert body["ignore_idle_window"] is True
                task = json.loads(self.contents[body["input_file_id"]])
                session = self.session(
                    {
                        "identity_id": task["identity_id"],
                        "template_id": task["template_id"],
                        "initial_events": [{"type": "user.message", "content": task["body"]["input"]}],
                    }
                )
                item = self.create(
                    "batch",
                    {
                        "status": "completed",
                        "output_file_id": "output",
                        "request_counts": {"total": 1, "completed": 1, "failed": 0},
                    },
                )
                self.outputs[item["id"]] = [
                    {
                        "custom_id": task["custom_id"],
                        "identity_id": task["identity_id"],
                        "template_id": task["template_id"],
                        "session_id": session["id"],
                        "status": "completed",
                        "response": task["body"]["input"],
                    }
                ]
            else:
                item = self.create(kind, body)
            return reply(item)
        if len(parts) == 3 and parts[-1] == "run":
            item = self.objects[parts[1]]
            session = self.session(item)
            execution = self.create("run", {"session_id": session["id"], "status": "completed"})
            return reply(execution)
        if len(parts) == 3 and parts[-1] == "tasks":
            return reply({"data": [{"custom_id": row["custom_id"]} for row in self.outputs[parts[1]]]})
        if len(parts) == 3 and parts[-1] == "clear":
            return reply({"status": "completed"})
        if verb == "DELETE" or (len(parts) == 3 and parts[-1] == "archive"):
            self.deleted.append(parts[1])
            return reply({})
        if len(parts) == 2 and verb == "GET":
            return reply(self.objects[parts[1]])
        raise AssertionError(f"Unexpected request: {verb} {path}")


def patch_batch_rows(monkeypatch, service):
    """离线回放时替换 batch 输出下载，避免真实网络请求。"""
    monkeypatch.setattr(forward_scenarios, "batch_rows", lambda client, batch_id: service.outputs[batch_id])
