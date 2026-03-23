# auto-training

Train models and agents to play 2048 with Python and `uv`.

## Quick Start

```bash
uv sync --all-groups
uv run auto-training
uv run pytest
uv run ruff check .
```

## Project Layout

- `src/auto_training/env/`: 2048 environment types and game logic
- `src/auto_training/models/`: model definitions and agent policies
- `src/auto_training/train/`: training loops and checkpoints
- `src/auto_training/eval/`: evaluation scripts and metrics
- `tests/`: smoke tests and environment correctness tests

## Current Status

The repo is bootstrapped with:

- a `uv`-managed package
- a minimal CLI entrypoint
- base environment scaffolding
- pytest and ruff configuration

## Next Steps

1. Implement deterministic 2048 move/merge logic.
2. Add random and heuristic baseline agents.
3. Add a first training baseline such as DQN.
