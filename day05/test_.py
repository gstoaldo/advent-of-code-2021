import pytest
from main import *


@pytest.mark.parametrize(
    "p1, p2, expected_cover_points",
    [
        (
            (1, 1),
            (1, 3),
            [
                (1, 1),
                (1, 2),
                (1, 3),
            ],
        ),
        (
            (1, 3),
            (1, 1),
            [
                (1, 1),
                (1, 2),
                (1, 3),
            ],
        ),
        (
            (1, 1),
            (3, 3),
            [
                (1, 1),
                (2, 2),
                (3, 3),
            ],
        ),
        (
            (9, 7),
            (7, 9),
            [
                (9, 7),
                (8, 8),
                (7, 9),
            ],
        ),
    ],
)
def test_cover_points(p1, p2, expected_cover_points):
    for point in get_cover_points(p1, p2):
        assert point in expected_cover_points


def test_diagram():
    diagram = Diagram(5)
    diagram.mark((0, 0))
    assert diagram.diagram[0][0] == 1

    diagram.mark((0, 0))
    assert diagram.diagram[0][0] == 2


def test_overlapping():
    diagram = Diagram(3)
    mark_line(diagram, (0, 1), (2, 1))
    mark_line(diagram, (1, 0), (1, 2))

    assert diagram.diagram[1][1] == 2
    assert diagram.n_overlaps() == 1


def test_part1():
    input = read_file("example.txt")
    assert get_overlaps(input, allow_diagonals=False) == 5


def test_part2():
    input = read_file("example.txt")
    assert get_overlaps(input, allow_diagonals=True) == 12
