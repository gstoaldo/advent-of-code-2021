import pytest
from main import *


def test_part1():
    input = parse("example.txt")
    assert run_simulation(input, 18)[0] == 26


def test_part2():
    input = parse("example.txt")
    assert run_simulation(input, 256)[0] == 26984457539


@pytest.mark.parametrize(
    "input, state",
    [
        ([3, 4, 3, 1, 2], [0, 1, 1, 2, 1, 0, 0, 0, 0]),
        ([2, 3, 2, 0, 1], [1, 1, 2, 1, 0, 0, 0, 0, 0]),
        ([1, 2, 1, 6, 0, 8], [1, 2, 1, 0, 0, 0, 1, 0, 1]),
    ],
)
def test_parse_to_state(input, state):
    assert parse_to_state(input) == state


@pytest.mark.parametrize(
    "state, next_state",
    [
        ([0, 1, 1, 2, 1, 0, 0, 0, 0], [1, 1, 2, 1, 0, 0, 0, 0, 0]),
        ([1, 1, 2, 1, 0, 0, 0, 0, 0], [1, 2, 1, 0, 0, 0, 1, 0, 1]),
    ],
)
def test_clock(state, next_state):
    assert clock(state) == next_state
