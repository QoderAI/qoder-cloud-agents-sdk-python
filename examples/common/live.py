from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
import time
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from uuid import uuid4

import httpx
from pydantic import ValidationError

from qca import APIError, APIResponseValidationError, APIStatusError


def name(kind: str) -> str:
    return f"sdk-python-{kind}-{uuid4().hex[:12]}"


def marker() -> str:
    return uuid4().hex


def read_env(path: str | Path) -> dict[str, str]:
    """Read assignments as data. Never evaluate shell expressions."""
    path = Path(path)
    if not path.exists():
        return {}
    values = {}
    for number, line in enumerate(path.read_text().splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        line = line.removeprefix("export ")
        key, sep, value = line.partition("=")
        if not sep or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key.strip()):
            raise ValueError(f"Invalid env assignment at line {number}")
        value = value.strip()
        if value.startswith(('"', "'")):
            end = value.find(value[0], 1)
            if end < 0:
                raise ValueError(f"Unterminated env value at line {number}")
            value = value[1:end]
        else:
            value = value.split(" #", 1)[0].strip()
        values[key.strip()] = value
    return values


@dataclass
class Config:
    mode: str
    access_token: str = field(repr=False)
    base_url: str = ""
    model: str = ""
    timeout: float = 300
    poll_interval: float = 1

    @classmethod
    def load(cls, mode: str, *, env_file: str = ".env.live", region: str | None = None, timeout: float = 300) -> Config:
        values = {**read_env(env_file), **os.environ}
        prefix = f"QODER_{mode.upper()}_"
        token = values.get(prefix + "PAT") or values.get("QODER_ACCESS_TOKEN", "")
        if not token:
            raise ValueError(f"Configure {prefix}PAT or QODER_ACCESS_TOKEN")
        suffix = "forward" if mode == "forward" else "cloud"
        base = (
            values.get(prefix + "BASE_URL")
            or (values.get("QODER_BASE_URL") if mode == "managed" else None)
            or f"https://api.qoder.com.cn/api/v1/{suffix}"
        )
        url = httpx.URL(base)
        if (
            url.scheme != "https"
            or url.host not in ("api.qoder.com", "api.qoder.com.cn")
            or url.userinfo
            or url.query
            or url.fragment
        ):
            raise ValueError("Examples require an HTTPS api.qoder.com.cn or api.qoder.com URL")
        if url.path.rstrip("/") != f"/api/v1/{suffix}":
            raise ValueError(f"Expected the {mode} API root /api/v1/{suffix}")
        if region:
            url = url.copy_with(host="api.qoder.com.cn" if region == "cn" else "api.qoder.com")
        if timeout <= 0:
            raise ValueError("timeout must be positive")
        return cls(mode, token, str(url), values.get(prefix + "MODEL", ""), timeout)

    def client_options(self) -> dict[str, Any]:
        return dict(access_token=self.access_token, base_url=self.base_url, max_retries=0, timeout=30)


def safe_error(error: BaseException, token: str = "") -> str:
    if isinstance(error, APIResponseValidationError):
        request_id = error.response.headers.get("x-request-id") or error.response.headers.get("request-id")
        text = (
            f"APIResponseValidationError: HTTP {error.status_code} {error.request.method} "
            f"{error.request.url.path} request_id={request_id}"
        )
        cause = error.__cause__
        if isinstance(cause, ValidationError):
            # Report the failing field and rule without exposing response values.
            for issue in cause.errors(include_url=False, include_input=False, include_context=False)[:5]:
                path = ".".join(str(part) for part in issue["loc"]) or "response"
                text += f"; {path}: {issue['type']} ({issue['msg']})"
    elif isinstance(error, APIStatusError):
        text = (
            f"HTTP {error.status_code} {error.request.method} {error.request.url.path} "
            f"code={error.code} type={error.type} request_id={error.request_id}"
        )
        body = error.body if isinstance(error.body, dict) else {}
        details = body.get("error", body)
        if isinstance(details, dict) and isinstance(details.get("message"), str):
            text += f" message={details['message']}"
    elif isinstance(error, (APIError, httpx.HTTPError)):
        text = type(error).__name__
    else:
        text = str(error)
    if token:
        text = text.replace(token, "[REDACTED]")
    return re.sub(r"https?://[^\s\"'<>]+", "[URL REDACTED]", text)[:1600]


class Run:
    def __init__(self, config: Config, *, verbose: bool = False) -> None:
        self.config = config
        self.verbose = verbose
        self.outputs: list[dict[str, Any]] = []
        self.deadline = time.monotonic() + config.timeout
        self.cleanups: list[tuple[str, str, Callable[[], Any]]] = []

    def output(self, label: str, value: Any) -> None:
        self.outputs.append({"label": label, "value": value})
        if self.verbose:
            text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, indent=2)
            separator = "\n" if "\n" in text else " "
            print(f"{label}:{separator}{text}", flush=True)

    def track(self, kind: str, resource_id: str, cleanup: Callable[[], Any]) -> str:
        if not resource_id:
            raise AssertionError(f"Created {kind} has no ID")
        self.cleanups.append((kind, resource_id, cleanup))
        self.output(f"{kind}_id", resource_id)
        return resource_id

    def remaining(self) -> float:
        remaining = self.deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError("Scenario deadline exceeded")
        return remaining

    def pause(self) -> None:
        time.sleep(min(self.remaining(), self.config.poll_interval))

    def cleanup(self) -> None:
        had_resources = bool(self.cleanups)
        failures = []
        for kind, resource_id, action in reversed(self.cleanups):
            # Each resource gets its own cleanup budget even if the scenario timed out.
            self.deadline = time.monotonic() + 60
            try:
                action()
            except Exception as error:
                failures.append(f"{kind} {resource_id}: {safe_error(error, self.config.access_token)}")
        self.cleanups.clear()
        if failures:
            raise RuntimeError("Cleanup failed:\n" + "\n".join(failures))
        if had_resources:
            self.output("cleanup", "completed")


@dataclass
class TurnResult:
    text: str = ""
    last_id: str = ""
    tool_used: bool = False
    complete: bool = False

    def observe(self, event: Any) -> None:
        if hasattr(event, "to_dict"):
            event = event.to_dict(mode="json")
        kind = event.get("type")
        if event.get("id"):
            self.last_id = event["id"]
        if kind in ("session.error", "session.status_terminated"):
            raise AssertionError(f"Execution failed: {kind}, event_id={self.last_id}")
        if kind in ("agent.tool_use", "agent.mcp_tool_use"):
            self.tool_used = True
        elif kind == "agent.message":
            # Only the latest completed assistant message can satisfy assertions.
            self.text = "\n".join(
                block.get("text", "") for block in event.get("content", []) if block.get("type") == "text"
            )
        elif kind == "session.status_idle":
            reason = event.get("stop_reason")
            reason = reason.get("type") if isinstance(reason, dict) else reason
            if reason not in (None, "", "end_turn", "stop_sequence"):
                raise AssertionError(f"Execution stopped early: {reason}, event_id={self.last_id}")
            self.complete = bool(self.text)

    def verify(self, expected: list[str], require_tool: bool = False) -> None:
        if not self.complete:
            raise AssertionError(f"No idle state after assistant output; last_event_id={self.last_id}")
        if not all(value in self.text for value in expected):
            raise AssertionError(f"Assistant output is missing expected values; last_event_id={self.last_id}")
        if require_tool and not self.tool_used:
            raise AssertionError(f"No actual tool execution; last_event_id={self.last_id}")


def wait_reply(events: Any, run: Run, session_id: str, after: str = "") -> TurnResult:
    result = TurnResult(last_id=after)
    while not result.complete:
        run.remaining()
        page = events.list(
            session_id,
            order="asc",
            limit=100,
            extra_query={"after_id": result.last_id or None, "include_tool_calls": True},
            timeout=min(run.remaining(), 30),
        )
        for index, event in enumerate(page):
            if index >= 2000:
                raise AssertionError("Event polling exceeded 2000 events")
            result.observe(event)
            if result.complete:
                break
        if not result.complete:
            run.pause()
    run.output("assistant", result.text)
    return result


def turn(
    events: Any,
    run: Run,
    session_id: str,
    prompt: str,
    expected: list[str],
    *,
    require_tool: bool = False,
) -> TurnResult:
    run.output("user", prompt)
    result = events.send(
        session_id,
        events=[{"type": "user.message", "content": [{"type": "text", "text": prompt}]}],
        extra_headers={"Idempotency-Key": name("event")},
    )
    if len(result.data) != 1 or not result.data[0].id:
        raise AssertionError("Send must return exactly one user event ID")
    reply = wait_reply(events, run, session_id, result.data[0].id)
    reply.verify(expected, require_tool)
    return reply


def choose_model(models: Any, requested: str) -> str:
    enabled = [model.id for model in models.data if model.is_enabled and model.id]
    if requested:
        if requested not in enabled:
            raise AssertionError("Configured model is not enabled for this account")
        return requested
    if not enabled:
        raise AssertionError("Account has no enabled models")
    return "ultimate" if "ultimate" in enabled else sorted(enabled)[0]


@dataclass
class ProjectMemory:
    project: str = field(default_factory=lambda: "青禾订单-" + marker()[:6])
    release_time: str = field(default_factory=lambda: f"{random.randrange(20, 24):02}:{random.randrange(60):02}")
    contact: str = field(default_factory=lambda: random.choice(["林岚", "陈朔", "叶澄", "苏棠"]))
    rollback_version: str = field(
        default_factory=lambda: f"v2.{random.randrange(100, 1000)}.{random.randrange(100, 1000)}"
    )
    path = "projects/release-conventions.md"

    def content(self) -> str:
        return f"---\nname: release-conventions\ndescription: {self.project} 的项目发布约定\nmetadata:\n  type: project\n---\n\n# {self.project}\n\n- 北京时间 {self.release_time} 开始发布。\n- 发布异常时联系值班负责人{self.contact}。\n- 回滚使用已验证的稳定版本 {self.rollback_version}。\n\nWhy: 在值班窗口发布，并使用验证过的版本恢复服务。\nHow to apply: 为这个项目拟定发布计划时遵循以上约定。\n"

    def index(self) -> str:
        return f"- [{self.project} 发布约定]({self.path}) — 发布窗口、异常联系人与回滚约定。\n"

    def prompt(self) -> str:
        return f"请根据你记得的项目约定，为「{self.project}」拟一份简短上线安排，涵盖开始时间、异常联系和回滚处理。不要执行发布；缺少信息时请明确说明。"

    def expected(self) -> list[str]:
        return [self.release_time, self.contact, self.rollback_version]


def run_cli(mode: str, client_type: Any, scenarios: dict[str, Callable[[Any, Run], None]]) -> None:
    parser = argparse.ArgumentParser(description=f"Qoder {mode} SDK examples")
    parser.add_argument("--env", default=".env.live")
    parser.add_argument("--region", choices=["cn", "international"])
    parser.add_argument("--scenario", choices=[*scenarios, "all"], default=next(iter(scenarios)))
    parser.add_argument("--timeout", type=float, default=300)
    parser.add_argument("--output", choices=["text", "json"], default="text")
    args = parser.parse_args()
    try:
        config = Config.load(mode, env_file=args.env, region=args.region, timeout=args.timeout)
    except Exception as error:
        parser.exit(2, safe_error(error) + "\n")
    results = []
    for scenario in scenarios if args.scenario == "all" else [args.scenario]:
        context = Run(config, verbose=args.output == "text")
        if args.output == "text":
            print(f"[{mode}.{scenario}]", flush=True)
        errors = []
        try:
            with client_type(**config.client_options()) as client:
                try:
                    scenarios[scenario](client, context)
                finally:
                    try:
                        context.cleanup()
                    except Exception as error:
                        errors.append(safe_error(error, config.access_token))
        except Exception as error:
            errors.insert(0, safe_error(error, config.access_token))
        results.append({"scenario": scenario, "passed": not errors, "outputs": context.outputs, "errors": errors})
        if args.output == "text":
            print(f"{scenario}: {'FAIL' if errors else 'PASS'}")
            for error in errors:
                print(error, file=sys.stderr)
    if args.output == "json":
        print(json.dumps(results, ensure_ascii=False, indent=2))
    raise SystemExit(1 if any(not result["passed"] for result in results) else 0)
