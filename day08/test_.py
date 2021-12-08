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
