import pytest
from main import Board, calc_number_calls

TEST_INPUT_CALLS = [
    7,
    4,
    9,
    5,
    11,
    17,
    23,
    2,
    0,
    14,
    21,
    24,
    10,
    16,
    13,
    6,
    15,
    25,
    12,
    22,
    18,
    20,
    8,
    19,
    3,
    26,
    1,
]
TEST_INPUT_BOARDS = [
    [
        [22, 13, 17, 11, 0],
        [8, 2, 23, 4, 24],
        [21, 9, 14, 16, 7],
        [6, 10, 3, 18, 5],
        [1, 12, 20, 15, 19],
    ],
    [
        [3, 15, 0, 2, 22],
        [9, 18, 13, 17, 5],
        [19, 8, 7, 25, 23],
        [20, 11, 10, 24, 4],
        [14, 21, 16, 12, 6],
    ],
    [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ],
]


@pytest.fixture
def board():
    return Board(
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


@pytest.mark.parametrize(
    "calls, boards, expected_winning_call, expected_unmarked_sum",
    [(TEST_INPUT_CALLS, TEST_INPUT_BOARDS, 24, 188)],
)
def test_calc_number_calls(calls, boards, expected_winning_call, expected_unmarked_sum):
    assert calc_number_calls(calls, boards) == (
        expected_winning_call,
        expected_unmarked_sum,
    )
