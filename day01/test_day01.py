import pytest
import main


@pytest.mark.parametrize(
    "input, expected_increases_count",
    [
        ((199, 200, 208, 210, 200, 207, 240, 269, 260, 263), 7),
        ((0, 0, 4, 4, 5), 2),
        ((10, 10, 8, 5, 10), 1),
    ],
)
def test_count_increases(input, expected_increases_count):
    assert main.count_increases(input) == expected_increases_count
