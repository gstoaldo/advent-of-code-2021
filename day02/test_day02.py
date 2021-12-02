import pytest
import main


@pytest.mark.parametrize(
    "input, expected_final_position, expected_position_product",
    [
        (
            [
                ("forward", 5),
                ("down", 5),
                ("forward", 8),
                ("up", 3),
                ("down", 8),
                ("forward", 2),
            ],
            [15, 10, 0],
            150,
        ),
        (
            [
                ("forward", 0),
                ("up", 10),
                ("up", 10),
                ("forward", 1),
            ],
            [1, -20, 0],
            -20,
        ),
        (
            [
                ("forward", 20),
                ("up", 10),
                ("down", 10),
                ("forward", 10),
            ],
            [30, 0, 0],
            0,
        ),
    ],
)
def test_calculate_final_position_without_aim(
    input, expected_final_position, expected_position_product
):
    final_position, position_product = main.calculate_final_position(
        input, main.step_parser_without_aim
    )
    assert final_position == expected_final_position
    assert position_product == expected_position_product


@pytest.mark.parametrize(
    "input, expected_final_position, expected_position_product",
    [
        (
            [
                ("forward", 5),
                ("down", 5),
                ("forward", 8),
                ("up", 3),
                ("down", 8),
                ("forward", 2),
            ],
            [15, 60, 10],
            900,
        ),
        (
            [
                ("up", 5),
                ("forward", 10),
                ("forward", 10),
            ],
            [20, -100, -5],
            -2000,
        ),
    ],
)
def test_calculate_final_position(
    input, expected_final_position, expected_position_product
):
    final_position, position_product = main.calculate_final_position(
        input, main.step_parser_with_aim, 1
    )
    assert final_position == expected_final_position
    assert position_product == expected_position_product
