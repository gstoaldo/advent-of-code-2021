import pytest
from main import *


@pytest.mark.parametrize(
    "fish_list, next_day_fish_list",
    [
        ([3, 4, 3, 1, 2], [2, 3, 2, 0, 1]),
        ([2, 3, 2, 0, 1], [1, 2, 1, 6, 0, 8]),
        (
            [0, 1, 0, 5, 6, 0, 1, 2, 2, 3, 7, 8],
            [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 7, 8, 8, 8],
        ),
    ],
)
def test_clock(fish_list, next_day_fish_list):
    assert clock(fish_list) == next_day_fish_list


def test_part1():
    input = parse("example.txt")
    # fmt: off
    final_state = [6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8] 
    assert run_simulation(input, 18) == (26, final_state)
