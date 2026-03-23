# agents.md

## Project Goal
- This repo is for experimenting with training models/agents to play 2048.
- Primary stack: Python.
- Dependency management: `uv`.
- Initial target: a clean local workflow for environment, training, evaluation, and iteration.

## Current Assumptions
- Start with single-machine training.
- Support CPU first; GPU support can be added later if useful.
- Focus on 4 actions: `up`, `down`, `left`, `right`.
- Prefer deterministic, testable game logic before larger model work.

## Engineering Rules
- Use `uv` for dependency and task management; do not introduce Poetry or Pipenv.
- Keep code under `src/`.
- Keep experiments reproducible: set seeds and keep config explicit.
- Separate game environment, model code, training loop, and evaluation code.
- Prefer small modules with type hints.
- Add tests for board transitions before adding complex training logic.

## Suggested Layout
- `src/auto_training/env/`: 2048 game state, move logic, reward, termination.
- `src/auto_training/models/`: policy/value models or other agents.
- `src/auto_training/train/`: trainers, rollout logic, checkpoints.
- `src/auto_training/eval/`: evaluation scripts and metrics.
- `src/auto_training/cli/`: local entrypoints.
- `tests/`: unit tests, especially environment correctness tests.
- `runs/`: local outputs, checkpoints, logs; should stay out of git if large.

## First Milestones
1. Implement a correct 2048 environment with tests.
2. Add baseline agents: random and simple heuristic.
3. Define observation format and reward strategy.
4. Add one training baseline, likely DQN first.
5. Add evaluation metrics such as max tile, average score, and survival length.

## Training Notes
- Treat environment correctness as the highest priority.
- Keep action masking explicit when a move is invalid.
- Make reward shaping easy to swap; do not hardcode one strategy everywhere.
- Save configs with checkpoints so runs are reproducible.
- Keep logging simple at first; CSV or JSONL is enough.

## Dependency Guidance
- Prefer minimal dependencies at the start.
- Likely early dependencies: `numpy`, `pytest`, and one DL stack when training begins.
- Add heavier packages only when they solve a concrete need.

## Collaboration Guidance
- When adding new code, include the simplest runnable path first.
- Do not optimize early for distributed training.
- If architecture is undecided, choose the option that keeps the environment API stable.
- If a change affects training semantics, update tests or add a small regression case.

## Definition of Done
- New components are runnable locally with `uv`.
- Core logic has basic tests.
- Commands and configs are discoverable from the repo root.
- Experimental code should not break the default training path.
