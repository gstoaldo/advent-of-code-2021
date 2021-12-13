import pytest
from main import *


@pytest.mark.parametrize(
    "dots, fy, expected",
    [
        ([(0, 0), (0, 5)], 3, [(0, 0), (0, 1)]),
        ([(0, 0), (0, 2)], 1, [(0, 0), (0, 0)]),
    ],
)
def test_fold_up(dots, fy, expected):
    assert fold_up(dots, fy) == expected


@pytest.mark.parametrize(
    "dots, fx, expected",
    [
        ([(1, 0), (4, 0)], 2, [(3, 0), (4, 0)]),
    ],
)
def test_fold_right(dots, fx, expected):
    assert fold_right(dots, fx) == expected


def test_cut_left():
    assert cut_left([(3, 0)], 2) == [(0, 0)]


def test_part1():
    dots, folds = parse("example.txt")
    new_dots = run_folds(dots, folds)
    print(new_dots)
    assert count_unique_dots(run_folds(dots, folds[:1])) == 17
