import pytest
from main import *


@pytest.mark.parametrize(
    "cuboid_range, cuboid",
    [
        (
            [(10, 10), (10, 10), (10, 10)],
            [(10, 10, 10)],
        ),
        (
            [(10, 11), (10, 11), (10, 11)],
            [
                (10, 10, 10),
                (10, 10, 11),
                (10, 11, 10),
                (10, 11, 11),
                (11, 10, 10),
                (11, 10, 11),
                (11, 11, 10),
                (11, 11, 11),
            ],
        ),
    ],
)
def test_range_to_cubes(cuboid_range, cuboid):
    assert range_to_cuboid(cuboid_range) == cuboid


def test_part1():
    steps = parse("example.txt")
    assert solve_part1(steps) == 590784
