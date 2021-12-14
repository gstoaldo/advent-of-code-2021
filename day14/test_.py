import pytest
from main import *


@pytest.mark.parametrize(
    "template, pairs, i, expected",
    [
        ("NNCB", {"NN": "C"}, 0, "NCN"),
        ("NNCB", {"NC": "B"}, 1, "NBC"),
    ],
)
def test_get_trio(template, pairs, i, expected):
    assert get_trio(template, pairs, i) == expected


def test_merge_trios():
    assert merge_trios(["NCN", "NBC", "CHB"]) == "NCNBCHB"


def test_step():
    assert step("NNCB", {"NN": "C", "NC": "B", "CB": "H"}) == "NCNBCHB"


def test_example():
    template, pairs = parse("example.txt")
    assert steps(template, pairs, 1) == "NCNBCHB"
    assert steps(template, pairs, 2) == "NBCCNBBBCBHCB"
    assert (
        steps(template, pairs, 4) == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
    )


def test_count_elements():
    assert count_elements("AAABBC") == {"A": 3, "B": 2, "C": 1}


def test_part1():
    template, pairs = parse("example.txt")
    assert solve_part1(template, pairs) == 1588
