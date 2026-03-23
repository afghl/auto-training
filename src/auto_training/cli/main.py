from __future__ import annotations

import argparse
from collections.abc import Sequence

from auto_training.env import GameConfig, empty_board


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="auto-training",
        description="Bootstrap utilities for training 2048 agents.",
    )
    parser.add_argument(
        "--board-size",
        type=int,
        default=4,
        help="Board size used for the smoke-test environment preview.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    config = GameConfig(board_size=args.board_size)
    board = empty_board(config)

    print("auto-training ready")
    print(f"board_size={config.board_size}")
    print(f"board_shape={board.shape}")
    print("next_step=implement_2048_transition_logic")
    return 0
