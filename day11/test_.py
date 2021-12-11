import pytest
from main import *

SAMPLE = [
    [1, 1, 1, 1, 1],
    [1, 9, 9, 9, 1],
    [1, 9, 1, 9, 1],
    [1, 9, 9, 9, 1],
    [1, 1, 1, 1, 1],
]


def test_get_adjacents():
    assert get_adjacents(SAMPLE, 0, 0) == [(0, 1), (1, 1), (1, 0)]
    assert get_adjacents(SAMPLE, 2, 2) == [
        (2, 3),
        (3, 3),
        (3, 2),
        (3, 1),
        (2, 1),
        (1, 1),
        (1, 2),
        (1, 3),
    ]


def test_full_energy_count():
    assert full_energy_count([[10, 1, 2], [9, 10, 4]]) == 2


def test_step():
    new_states, flash_count = step(SAMPLE)
    assert new_states == [
        [3, 4, 5, 4, 3],
        [4, 0, 0, 0, 4],
        [5, 0, 0, 0, 5],
        [4, 0, 0, 0, 4],
        [3, 4, 5, 4, 3],
    ]
    assert flash_count == 9


def test_part1():
    input = parse("example.txt")
    assert run_steps(input, 100) == 1656
