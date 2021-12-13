import pytest
from main import *


TEST_CASES = [
    (
        {
            "start": ["end"],
            "end": [],
        },
        [["start", "end"]],
    ),
    (
        {
            "start": ["end", "b"],
            "b": ["end"],
            "end": [],
        },
        [["start", "end"], ["start", "b", "end"]],
    ),
    (
        {
            "start": ["end", "b", "c"],
            "b": ["end"],
            "c": ["end"],
            "end": [],
        },
        [["start", "end"], ["start", "b", "end"], ["start", "c", "end"]],
    ),
    (
        {
            "start": ["end", "b"],
            "b": ["end", "c"],
            "c": ["end"],
            "end": [],
        },
        [["start", "end"], ["start", "b", "end"], ["start", "b", "c", "end"]],
    ),
    (
        {
            "start": ["A"],
            "A": ["end", "c"],
            "c": ["A"],
            "end": [],
        },
        [["start", "A", "end"], ["start", "A", "c", "A", "end"]],
    ),
    (
        {
            "start": ["B", "c"],
            "B": ["end"],
            "c": ["end"],
            "end": [],
        },
        [["start", "B", "end"], ["start", "c", "end"]],
    ),
    (
        {
            "start": ["A", "b"],
            "A": ["end", "b"],
            "b": ["A", "end"],
            "end": [],
        },
        [
            ["start", "A", "end"],
            ["start", "A", "b", "A", "end"],
            ["start", "A", "b", "end"],
            ["start", "b", "A", "end"],
            ["start", "b", "end"],
        ],
    ),
]


@pytest.mark.parametrize("graph, expected", TEST_CASES)
def test_get_paths(graph, expected):
    paths = get_paths(graph)
    assert all(path in expected for path in paths)


def test_part1():
    graph = parse("small-example.txt")
    paths = get_paths(graph)
    assert len(paths) == 10

    graph = parse("medium-example.txt")
    paths = get_paths(graph)
    assert len(paths) == 19

    graph = parse("big-example.txt")
    paths = get_paths(graph)
    assert len(paths) == 226
