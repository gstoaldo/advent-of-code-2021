import pytest
from main import *


@pytest.mark.parametrize(
    "output_values, expected_count",
    [
        (["fdgacbe", "cefdb", "cefbgd", "gcbe"], 2),
        (["gecf", "egdcabf", "bgf", "bfgea"], 3),
    ],
)
def test_count_unique_segments(output_values, expected_count):
    assert count_unique_segments(output_values) == expected_count


def test_part1():
    input = parse("example.txt")
    assert count_output_unique_segments(input) == 26


@pytest.mark.parametrize(
    "signals, char, expected_count",
    [
        (["af", "bf", "gf"], "f", 3),
        (["af", "bf", "gf"], "a", 1),
    ],
)
def test_segment_freq(signals, char, expected_count):
    assert segment_freq(signals)[char] == expected_count


@pytest.mark.parametrize(
    "signals, count, expected_char",
    [
        (["af", "bf", "gf"], 3, ["f"]),
        (["af", "bf", "gf"], 1, ["a", "b", "g"]),
    ],
)
def test_segment_by_count(signals, count, expected_char):
    assert segment_by_count(signals, count) == expected_char


def test_get_signals_translation():
    signals = [
        "acedgfb",
        "cdfbe",
        "gcdfa",
        "fbcad",
        "dab",
        "cefabd",
        "cdfgeb",
        "eafb",
        "cagedb",
        "ab",
    ]
    assert get_signals_translation(signals) == {
        "acedgfb": 8,
        "cdfbe": 5,
        "gcdfa": 2,
        "fbcad": 3,
        "dab": 7,
        "cefabd": 9,
        "cdfgeb": 6,
        "eafb": 4,
        "cagedb": 0,
        "ab": 1,
    }


def test_part2():
    assert sum_outputs(parse("example.txt")) == 61229
