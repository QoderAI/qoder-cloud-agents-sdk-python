PYTHON ?= python3
LIVE_ENV_FILE ?= .env.live
.DEFAULT_GOAL := test

.PHONY: test lint typecheck build docs docs-check test-live test-live-managed test-live-all

test:
	$(PYTHON) -m pytest -q

docs:
	uv run --python 3.12 --extra dev --locked python scripts/generate-docs.py

docs-check:
	uv run --python 3.12 --extra dev --locked python scripts/docs-check.py

lint:
	$(PYTHON) -m ruff check src tests examples scripts
	$(PYTHON) -m ruff format --check src tests examples scripts

typecheck:
	$(PYTHON) -m mypy src/qca scripts

build:
	$(PYTHON) -m build

test-live:
	QODER_RUN_LIVE=1 QODER_LIVE_ENV_FILE="$(LIVE_ENV_FILE)" $(PYTHON) -m pytest tests/integration/test_forward.py -m integration -v

test-live-managed:
	QODER_RUN_LIVE=1 QODER_LIVE_ENV_FILE="$(LIVE_ENV_FILE)" $(PYTHON) -m pytest tests/integration/test_managed.py -m integration -v

test-live-all:
	QODER_RUN_LIVE=1 QODER_LIVE_ENV_FILE="$(LIVE_ENV_FILE)" $(PYTHON) -m pytest tests/integration -m integration -v
