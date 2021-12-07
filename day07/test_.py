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
