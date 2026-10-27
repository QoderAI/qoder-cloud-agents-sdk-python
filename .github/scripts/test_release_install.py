import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

WORKFLOW = Path(__file__).resolve().parents[1] / "workflows" / "release.yml"


def install_step():
    lines = WORKFLOW.read_text().splitlines()
    start = lines.index("      - name: Verify the installed public package") + 1
    run = lines.index("        run: |", start) + 1
    end = run
    while end < len(lines) and (not lines[end].strip() or lines[end].startswith("          ")):
        end += 1
    return "\n".join(line[10:] for line in lines[run:end]) + "\n"


FAKE_PYTHON = """\
import json
import os
import sys
from pathlib import Path

root = Path(os.environ["TEST_ROOT"])
args = sys.argv[1:]
with (root / "calls.jsonl").open("a") as calls:
    calls.write(json.dumps(args) + "\\n")
if args[:2] == ["-m", "venv"]:
    venv = Path(args[2])
    (root / "venv-path").write_text(str(venv))
    (venv / "bin").mkdir()
    (venv / "bin" / "python").symlink_to(Path(__file__).resolve())
elif args[:3] == ["-m", "pip", "install"]:
    counter = root / "attempts"
    attempt = int(counter.read_text()) if counter.exists() else 0
    counter.write_text(str(attempt + 1))
    outcomes = json.loads(os.environ["PIP_OUTCOMES"])
    status, output = outcomes[min(attempt, len(outcomes) - 1)]
    print(output, file=sys.stderr if status else sys.stdout)
    raise SystemExit(status)
elif args == ["-"]:
    (root / "import-check.py").write_text(sys.stdin.read())
    raise SystemExit(int(os.environ.get("IMPORT_STATUS", "0")))
else:
    raise SystemExit(f"Unexpected Python arguments: {args}")
"""


class PublicInstallTests(unittest.TestCase):
    missing = (1, "ERROR: No matching distribution found for qca-sdk==0.12.0")

    def run_install(self, outcomes, *, import_status=0):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            binary = root / "python"
            binary.write_text(f"#!{sys.executable}\n" + FAKE_PYTHON)
            binary.chmod(0o755)
            sleep = root / "sleep"
            sleep.write_text('#!/bin/sh\nprintf "%s\\n" "$1" >> "$TEST_ROOT/sleeps"\n')
            sleep.chmod(0o755)
            env = dict(
                os.environ,
                PATH=f"{root}{os.pathsep}{os.environ['PATH']}",
                TEST_ROOT=str(root),
                PIP_OUTCOMES=json.dumps(outcomes),
                IMPORT_STATUS=str(import_status),
                PACKAGE_NAME="qca-sdk",
                RELEASE_VERSION="0.12.0",
                PYPI_INDEX_URL="https://pypi.org/simple/",
                GITHUB_STEP_SUMMARY=str(root / "summary"),
            )
            result = subprocess.run(["bash", "-c", install_step()], env=env, capture_output=True, text=True, timeout=30)
            calls = [json.loads(line) for line in (root / "calls.jsonl").read_text().splitlines()]
            installs = [args for args in calls if args[:3] == ["-m", "pip", "install"]]
            for command in installs:
                self.assertIn("--no-cache-dir", command)
                self.assertEqual(command[-3:], ["--index-url", "https://pypi.org/simple/", "qca-sdk==0.12.0"])
            self.assertFalse(Path((root / "venv-path").read_text()).exists(), "Temporary venv must be removed")
            sleeps = (root / "sleeps").read_text().splitlines() if (root / "sleeps").exists() else []
            summary = (root / "summary").read_text() if (root / "summary").exists() else ""
            return result, len(installs), sleeps, calls.count(["-"]), summary

    def test_available_release_installs_once_and_checks_imports(self):
        result, attempts, sleeps, imports, summary = self.run_install([(0, "Installed")])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((attempts, sleeps, imports), (1, [], 1))
        self.assertIn("Verified clean installation", summary)

    def test_index_lag_retries_then_checks_imports(self):
        result, attempts, sleeps, imports, summary = self.run_install([self.missing, self.missing, (0, "Installed")])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((attempts, sleeps, imports), (3, ["30", "30"], 1))
        self.assertIn("attempt 3/21", result.stdout)
        self.assertIn("Verified clean installation", summary)

    def test_unavailable_release_exhausts_limit_without_imports_or_success(self):
        result, attempts, sleeps, imports, summary = self.run_install([self.missing])
        self.assertEqual(result.returncode, 1)
        self.assertEqual((attempts, sleeps, imports, summary), (21, ["30"] * 20, 0, ""))
        self.assertIn("still unavailable", result.stderr)
        self.assertIn(self.missing[1], result.stderr)

    def test_other_install_errors_fail_immediately(self):
        for message in (
            "ERROR: No matching distribution found for httpx==999",
            "ERROR: No matching distribution found for qca-sdk==0.12.01",
            "ERROR: THESE PACKAGES DO NOT MATCH THE HASHES FROM THE REQUIREMENTS FILE.",
            "ERROR: ResolutionImpossible",
        ):
            with self.subTest(message=message):
                result, attempts, sleeps, imports, summary = self.run_install([(2, message)])
                self.assertEqual(result.returncode, 2)
                self.assertEqual((attempts, sleeps, imports, summary), (1, [], 0, ""))
                self.assertIn(message, result.stderr)

    def test_import_failure_is_not_retried_or_reported_as_success(self):
        result, attempts, sleeps, imports, summary = self.run_install([(0, "Installed")], import_status=3)
        self.assertEqual(result.returncode, 3)
        self.assertEqual((attempts, sleeps, imports, summary), (1, [], 1, ""))

    def test_install_step_has_wall_clock_limit(self):
        lines = WORKFLOW.read_text().splitlines()
        start = lines.index("      - name: Verify the installed public package") + 1
        run = lines.index("        run: |", start)
        self.assertIn("        timeout-minutes: 15", lines[start:run])


if __name__ == "__main__":
    unittest.main()
