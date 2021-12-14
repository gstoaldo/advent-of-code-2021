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


###


def test_count_pairs():
    assert count_pairs("NNCB", {"NN": "C", "NC": "B", "CB": "H"}) == {
        "NN": 1,
        "NC": 1,
        "CB": 1,
    }


def test_step_optimized():
    template, pairs = parse("example.txt")
    count = step_optimized(count_pairs(template, pairs), pairs)
    assert count["NC"] == 1
    assert count["CN"] == 1
    assert count["NB"] == 1
    assert count["BC"] == 1
    assert count["CH"] == 1
    assert count["HB"] == 1

    count = step_optimized(count_pairs("NNNN", pairs), pairs)
    assert count["NC"] == 3
    assert count["CN"] == 3
    assert count["NN"] == 0


def test_count_chars():
    assert count_chars({"NC": 3, "CN": 3}) == {"N": 6, "C": 6}


def test_part2():
    template, pairs = parse("example.txt")
    assert solve_part2(template, pairs) == 2188189693529
