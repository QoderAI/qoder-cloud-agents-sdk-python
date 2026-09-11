PYTHON ?= python3
LIVE_ENV_FILE ?= .env.live
.DEFAULT_GOAL := test

.PHONY: test lint typecheck build test-live test-live-managed test-live-all

test:
	$(PYTHON) -m pytest -q

lint:
	$(PYTHON) -m ruff check src tests examples
	$(PYTHON) -m ruff format --check src tests examples

typecheck:
	$(PYTHON) -m mypy src/qca

build:
	$(PYTHON) -m build

test-live:
	QODER_RUN_LIVE=1 QODER_LIVE_ENV_FILE="$(LIVE_ENV_FILE)" $(PYTHON) -m pytest examples/forward -m live -v

test-live-managed:
	QODER_RUN_LIVE=1 QODER_LIVE_ENV_FILE="$(LIVE_ENV_FILE)" $(PYTHON) -m pytest examples/managed -m live -v

test-live-all:
	QODER_RUN_LIVE=1 QODER_LIVE_ENV_FILE="$(LIVE_ENV_FILE)" $(PYTHON) -m pytest examples -m live -v
