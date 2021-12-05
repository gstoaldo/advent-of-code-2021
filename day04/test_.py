import pytest
import main


@pytest.fixture
def board():
    return main.Board(
        [
            [6, 2, 3],
            [2, 1, 6],
            [2, 0, 0],
        ]
    )


def test_mark(board):
    board.mark(2)
    assert board.marks == [
        [False, True, False],
        [True, False, False],
        [True, False, False],
    ]


def test_bingo(board):
    assert board.unmarked_sum() == 22

    board.mark(3)
    assert not board.bingo()
    assert board.unmarked_sum() == 19

    board.mark(6)
    assert not board.bingo()
    assert board.unmarked_sum() == 7

    board.mark(0)
    assert board.bingo()
    assert board.unmarked_sum() == 7


def test_part1():
    calls, boards = main.read_file("example.txt")
    assert main.calc_first_bingo(calls, boards) == (24, 188)
    assert main.calc_score(calls, boards, main.calc_first_bingo) == 4512


def test_part2():
    calls, boards = main.read_file("example.txt")
    assert main.calc_last_bingo(calls, boards) == (13, 148)
    assert main.calc_score(calls, boards, main.calc_last_bingo) == 1924
