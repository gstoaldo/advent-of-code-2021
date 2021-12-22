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


@pytest.mark.parametrize(
    "range_a, range_b, expected",
    [
        ((1, 10), (20, 30), False),
        ((1, 5), (5, 10), (5, 5)),
        ((1, 10), (8, 30), (8, 10)),
        ((1, 1), (1, 1), (1, 1)),
    ],
)
def test_get_1D_intersection(range_a, range_b, expected):
    assert get_1D_intersection(range_a, range_b) == expected


# @pytest.mark.parametrize(
#     "range_a, range_b, expected",
#     [
#         (
#             [(1, 5), (1, 5), (1, 5)],
#             [(10, 15), (10, 15), (10, 15)],
#             False,
#         ),
#         (
#             [(1, 5), (1, 5), (1, 5)],
#             [(3, 15), (10, 15), (3, 15)],
#             False,
#         ),
#         (
#             [(1, 5), (1, 5), (1, 5)],
#             [(3, 15), (1, 15), (3, 15)],
#             [(3, 5), (1, 5), (3, 5)],
#         ),
#     ],
# )
# def test_get_3D_intersection(range_a, range_b, expected):
#     assert get_3D_intersection(range_a, range_b) == expected


# def test_count_cubes():
#     assert count_cubes([(1, 3), (1, 3), (1, 3)]) == 27


@pytest.mark.parametrize(
    "steps, expected",
    [
        (
            [
                ("on", [(10, 12), (10, 12), (10, 12)]),
            ],
            27,
        ),
        (
            [
                ("on", [(10, 12), (10, 12), (10, 12)]),
                ("on", [(10, 12), (10, 12), (10, 12)]),
            ],
            27,
        ),
        (
            [
                ("off", [(10, 12), (10, 12), (10, 12)]),
            ],
            0,
        ),
        (
            [
                ("on", [(10, 12), (10, 12), (10, 12)]),
                ("off", [(10, 12), (10, 12), (10, 12)]),
                ("on", [(10, 12), (10, 12), (10, 12)]),
            ],
            27,
        ),
        (
            [
                ("on", [(10, 12), (10, 12), (10, 12)]),
                ("off", [(10, 12), (10, 12), (10, 12)]),
                ("off", [(10, 12), (10, 12), (10, 12)]),
                ("on", [(10, 12), (10, 12), (10, 12)]),
            ],
            27,
        ),
        (
            [
                ("on", [(10, 12), (10, 12), (10, 12)]),
                ("on", [(11, 13), (11, 13), (11, 13)]),
            ],
            46,
        ),
        (
            [
                ("on", [(10, 12), (10, 12), (10, 12)]),
                ("on", [(11, 13), (11, 13), (11, 13)]),
                ("off", [(9, 11), (9, 11), (9, 11)]),
            ],
            38,
        ),
        (
            [
                ("on", [(10, 12), (10, 12), (10, 12)]),
                ("off", [(10, 12), (10, 12), (10, 12)]),
                ("off", [(10, 12), (10, 12), (10, 12)]),
            ],
            0,
        ),
        (
            [
                ("on", [(10, 12), (10, 12), (10, 12)]),
                ("off", [(10, 12), (10, 12), (10, 12)]),
                ("off", [(10, 12), (10, 12), (10, 12)]),
                ("on", [(10, 10), (10, 10), (10, 10)]),
            ],
            1,
        ),
        (
            [
                ("off", [(10, 12), (10, 12), (10, 12)]),
                ("on", [(10, 10), (10, 10), (10, 10)]),
                ("on", [(10, 10), (10, 10), (10, 10)]),
            ],
            1,
        ),
    ],
)
def test_part2(steps, expected):
    assert solve_part2(steps) == expected


def test_part2_example():
    steps = parse("big-example.txt")
    assert solve_part2(steps) == 2758514936282235
