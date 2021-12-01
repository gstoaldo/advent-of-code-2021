import pytest
import main

# part 1
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


# part 2
@pytest.mark.parametrize(
    "input, expected_increases_count",
    [
        ((199, 200, 208, 210, 200, 207, 240, 269, 260, 263), 5),
        ((0, 0, 6, 2), 1),
        ((0, 0, 6, 2, 1, 1), 2),
        ((1, 1, 1, 1, 1, 1), 0),
    ],
)
def test_count_window_increases(input, expected_increases_count):
    assert main.count_window_increases(input) == expected_increases_count


@pytest.mark.parametrize(
    "input, index, expected_sum",
    [
        ((199, 200, 208, 210, 200, 207, 240, 269, 260, 263), 2, 607),
        ((199, 200, 208, 210, 200, 207, 240, 269, 260, 263), 3, 618),
        ((199, 200, 208, 210, 200, 207, 240, 269, 260, 263), 9, 792),
    ],
)
def test_sum_window(input, index, expected_sum):
    assert main.sum_window(input, index, window_length=3) == expected_sum
