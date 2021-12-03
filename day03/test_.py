import pytest
from main import count_bits, calc_rates


@pytest.mark.parametrize(
    "input, expected_zero_count, expected_one_count",
    [
        (
            [
                "00100",
                "11110",
                "10110",
                "10111",
                "10101",
                "01111",
                "00111",
                "11100",
                "10000",
                "11001",
                "00010",
                "01010",
            ],
            [5, 7, 4, 5, 7],
            [7, 5, 8, 7, 5],
        ),
        (
            [
                "001",
                "000",
            ],
            [2, 2, 1],
            [0, 0, 1],
        ),
    ],
)
def test_count_bits(input, expected_zero_count, expected_one_count):
    assert count_bits(input) == (expected_zero_count, expected_one_count)


@pytest.mark.parametrize(
    "zero_count, one_count, expected_gamma_rate, expected_epsilon_rate",
    [
        ([5, 7, 4, 5, 7], [7, 5, 8, 7, 5], ("10110", 22), ("01001", 9)),
        ([2, 2, 1], [0, 0, 1], ("000", 0), ("111", 7)),
    ],
)
def test_calc_rates(zero_count, one_count, expected_gamma_rate, expected_epsilon_rate):
    assert calc_rates(zero_count, one_count) == (
        expected_gamma_rate,
        expected_epsilon_rate,
    )
