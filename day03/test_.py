import pytest
from main import (
    count_bits,
    calc_rates,
    filter_by_bit_count,
    calc_o2_generator_rating,
    calc_co2_scrubber_rating,
)

TEST_INPUT = [
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
]


@pytest.mark.parametrize(
    "input, expected_zero_count, expected_one_count",
    [
        (
            TEST_INPUT,
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


@pytest.mark.parametrize(
    "input, index, expected",
    [
        (
            ["001", "000", "100"],
            0,
            ["001", "000"],
        ),
        (
            ["001", "000", "100"],
            1,
            ["001", "000", "100"],
        ),
        (
            ["001", "001", "101", "000"],
            2,
            ["001", "001", "101"],
        ),
    ],
)
def test_filter_by_bit_count(input, index, expected):
    assert filter_by_bit_count(input, index) == expected


@pytest.mark.parametrize(
    "input, expected_o2, expected_co2",
    [
        (TEST_INPUT, ("10111", 23), ("01010", 10)),
    ],
)
def test_calc_gas_rating(input, expected_o2, expected_co2):
    assert calc_o2_generator_rating(input) == expected_o2
    assert calc_co2_scrubber_rating(input) == expected_co2
