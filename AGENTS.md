# Repository Guidelines

## Project Structure & Module Organization
- Source code: `are/` (core in `are/simulation/` with `apps/`, `agents/`, `scenarios/`, `utils/`, `benchmark/`, `gui/`, and `tests/`).
- Tests: `are/simulation/tests/` (mix of `test_*.py` and `*_test.py`).
- Docs: `docs/`; Build hooks: `build_hooks/` (GUI build script).
- Packaging/config: `pyproject.toml`, `requirements*.txt`, `uv.lock`, `example.env`, `Dockerfile`.

## Build, Test, and Development Commands
- Setup (uv recommended): `uv pip install -r requirements.txt` (add `-r requirements-dev.txt` for dev).
- Lint/format: `uvx ruff check --fix .` and `uvx ruff format .`.
- Type check: `uv run --extra dev pyright`.
- Tests: `pytest -q are/simulation/tests` (run subsets with `-k <expr>`).
- Run scenarios: `are-run -s scenario_tutorial -a default`.
- Benchmark: `are-benchmark gaia2-run --hf meta-agents-research-environments/gaia2 -l 1`.
- GUI: `are-gui -s scenario_find_image_file` (serves locally, typically on port 8080).

## Coding Style & Naming Conventions
- Python: 4-space indent, type hints required for public APIs, docstrings on modules/classes/functions.
- Naming: modules/files `snake_case.py`; classes `CamelCase`; functions/vars `snake_case`.
- Tools: Ruff for linting/import-sort/formatting; Pyright for type checking; pre-commit is configured.

## Testing Guidelines
- Framework: `pytest` with assertions and fixtures; keep tests close to subject in `are/simulation/tests/`.
- Naming: prefer `test_*.py` (or existing `*_test.py`) with descriptive test functions.
- Coverage: add tests for new code paths and edge cases; include negative tests for validation logic.
- Run fast locally: `pytest -q`; use `-k`/`-m` to filter.

## Commit & Pull Request Guidelines
- Commits: imperative present tense (“Add”, “Fix”), concise subject, context in body if needed.
- Pre-submit: run lint, format, type check, and tests; attach CLI examples or screenshots for UX/GUI changes.
- PRs: clear description, linked issues, rationale, and testing notes; update docs/tutorials if APIs or behavior change.
- CLA: follow CONTRIBUTING/CLA instructions when opening your first PR.

## Security & Configuration Tips
- Secrets via env vars (see `example.env`); never commit keys.
- Model providers: configure via env/flags when running `are-benchmark`/`are-run`.
- GUI client dev: see `are/simulation/gui/client/` (use npm tooling); GUI assets build during packaging via `build_hooks` when `BUILD_GUI=1`.

