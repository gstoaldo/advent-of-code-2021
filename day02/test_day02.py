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
            [15, 10],
            150,
        ),
        (
            [
                ("forward", 0),
                ("up", 10),
                ("up", 10),
                ("forward", 1),
            ],
            [1, -20],
            -20,
        ),
        (
            [
                ("forward", 20),
                ("up", 10),
                ("down", 10),
                ("forward", 10),
            ],
            [30, 0],
            0,
        ),
    ],
)
def test_calculate_final_position(
    input, expected_final_position, expected_position_product
):
    final_position, position_product = main.calculate_final_position(input)
    assert final_position == expected_final_position
    assert position_product == expected_position_product
