from math import exp
import pytest
from main import *


def test_adjacents():
    sample = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    assert list(get_adjacents(sample, *(0, 0))) == [(0, 1), (1, 0)]
    assert list(get_adjacents(sample, 1, 1)) == [(1, 2), (1, 0), (2, 1), (0, 1)]


@pytest.mark.parametrize(
    "matrix, start, end, expected",
    [
        (
            [[1, 2], [3, 4]],
            (0, 0),
            (0, 1),
            [(0, 0), (0, 1)],
        ),
        (
            [[1, 2, 3], [4, 5, 6]],
            (0, 0),
            (0, 2),
            [(0, 0), (0, 1), (0, 2)],
        ),
    ],
)
def test_paths(matrix, start, end, expected):
    path = get_path(matrix, start, end)
    assert path == expected


def test_part1():
    matrix = parse("example.txt")
    assert solve_part1(matrix) == 40
