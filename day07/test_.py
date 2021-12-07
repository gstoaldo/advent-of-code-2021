import pytest
from main import *


@pytest.mark.parametrize(
    "crabs, position, expected_fuel",
    [
        ([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 2, 37),
        ([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 1, 41),
        ([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 10, 71),
    ],
)
def test_total_fuel(crabs, position, expected_fuel):
    assert total_fuel(crabs, position) == expected_fuel


def test_part1():
    input = parse("example.txt")
    assert find_best_position(input) == (37, 2)


@pytest.mark.parametrize(
    "position, position_to_move, expected_fuel",
    [
        (16, 5, 66),
        (1, 5, 10),
        (2, 5, 6),
        (0, 5, 15),
        (14, 5, 45),
    ],
)
def test_not_constant_eq(position, position_to_move, expected_fuel):
    assert not_constant_eq(position, position_to_move) == expected_fuel


def test_part2():
    input = parse("example.txt")
    assert find_best_position(input, move_eq=not_constant_eq) == (168, 5)
