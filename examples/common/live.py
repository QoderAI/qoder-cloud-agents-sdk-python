from __future__ import annotations

import argparse
import json
import os
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
    pat: str = field(repr=False)
    base_url: str = ""
    model: str = ""
    timeout: float = 300
    poll_interval: float = 1

    @classmethod
    def load(cls, mode: str, *, env_file: str = ".env.live", region: str | None = None, timeout: float = 300) -> Config:
        values = {**read_env(env_file), **os.environ}
        prefix = f"QODER_{mode.upper()}_"
        token = values.get(prefix + "PAT") or values.get("QODER_PAT", "")
        if not token:
            raise ValueError(f"Configure {prefix}PAT or QODER_PAT")
        suffix = "forward" if mode == "forward" else "cloud"
        base = values.get(prefix + "BASE_URL") or f"https://api.qoder.com.cn/api/v1/{suffix}"
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
        return dict(pat=self.pat, base_url=self.base_url, max_retries=0, timeout=30)


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
                failures.append(f"{kind} {resource_id}: {safe_error(error, self.config.pat)}")
        self.cleanups.clear()
        if failures:
            raise RuntimeError("Cleanup failed:\n" + "\n".join(failures))
        if had_resources:
            self.output("cleanup", "completed")


def choose_model(models: Any, requested: str) -> str:
    enabled = [model.id for model in models.data if model.is_enabled and model.id]
    if requested:
        if requested not in enabled:
            raise AssertionError("Configured model is not enabled for this account")
        return requested
    if not enabled:
        raise AssertionError("Account has no enabled models")
    return "ultimate" if "ultimate" in enabled else sorted(enabled)[0]


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
                        errors.append(safe_error(error, config.pat))
        except Exception as error:
            errors.insert(0, safe_error(error, config.pat))
        results.append({"scenario": scenario, "passed": not errors, "outputs": context.outputs, "errors": errors})
        if args.output == "text":
            print(f"{scenario}: {'FAIL' if errors else 'PASS'}")
            for error in errors:
                print(error, file=sys.stderr)
    if args.output == "json":
        print(json.dumps(results, ensure_ascii=False, indent=2))
    raise SystemExit(1 if any(not result["passed"] for result in results) else 0)
