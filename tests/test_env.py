import numpy as np
import pytest

from auto_training.env import GameConfig, empty_board


def test_empty_board_uses_expected_shape_and_dtype() -> None:
    board = empty_board(GameConfig(board_size=4))

    assert board.shape == (4, 4)
    assert board.dtype == np.int32
    assert np.count_nonzero(board) == 0


def test_game_config_rejects_invalid_spawn_configuration() -> None:
    with pytest.raises(ValueError, match="same length"):
        GameConfig(spawn_values=(2, 4), spawn_weights=(1.0,))

    with pytest.raises(ValueError, match="sum to 1.0"):
        GameConfig(spawn_values=(2, 4), spawn_weights=(0.7, 0.1))
