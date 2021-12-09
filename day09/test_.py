import pytest
from main import *

SAMPLE = [
    [1, 9, 2],
    [3, 2, 3],
    [2, 9, 4],
]


@pytest.mark.parametrize(
    "input, i, j, expected_is_local_min",
    [
        (SAMPLE, 0, 0, True),
        (SAMPLE, 0, 1, False),
        (SAMPLE, 1, 1, True),
    ],
)
def test_is_local_min(input, i, j, expected_is_local_min):
    assert is_local_min(input, i, j) == expected_is_local_min


@pytest.mark.parametrize(
    "input, i, j, expected_adjacents",
    [
        (SAMPLE, 0, 0, [9, 3]),
        (SAMPLE, 0, 1, [2, 1, 2]),
        (SAMPLE, 1, 1, [3, 3, 9, 9]),
    ],
)
def test_get_adjacents(input, i, j, expected_adjacents):
    assert get_adjacents(input, i, j) == expected_adjacents


def test_part1():
    input = parse("example.txt")
    assert get_local_mins(input) == [1, 0, 5, 5]
    assert risk_level_sum(input) == 15
