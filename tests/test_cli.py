from auto_training.cli.main import main


def test_main_smoke(capsys) -> None:
    exit_code = main([])

    captured = capsys.readouterr()

    assert exit_code == 0
    assert "auto-training ready" in captured.out
    assert "board_shape=(4, 4)" in captured.out


def test_main_accepts_board_size(capsys) -> None:
    main(["--board-size", "5"])

    captured = capsys.readouterr()

    assert "board_size=5" in captured.out
    assert "board_shape=(5, 5)" in captured.out
