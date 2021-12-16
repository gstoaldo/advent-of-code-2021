import pytest
from main import *


def test_hex_to_binary():
    assert hex_to_binary("D2FE28") == "110100101111111000101000"


def test_parse_header():
    assert parse_header("110100101111111000101000") == (
        6,
        4,
        None,
        "101111111000101000",
    )


def test_parse_literal():
    assert parse_literal("101111111000101000") == (2021, "000")
    assert parse_literal("0101000") == (10, "00")


def test_example1():
    ex = "D2FE28"
    assert parse_message(hex_to_binary(ex)) == (6, [2021])


def test_parse_length_id_zero():
    assert parse_length_id_zero(
        "0000000000110111101000101001010010001001000000000"
    ) == (
        27,
        "1101000101001010010001001000000000",
    )


def test_example2():
    ex = "38006F45291200"
    assert parse_message(hex_to_binary(ex)) == (1 + 6 + 2, [10, 20])


def test_parse_length_id_one():
    assert parse_length_id_one("0000000001101010000001100100000100011000001100000") == (
        3,
        "01010000001100100000100011000001100000",
    )


@pytest.mark.parametrize(
    "hex, version_sum",
    [
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    ],
)
def test_part1(hex, version_sum):
    assert parse_message(hex_to_binary(hex))[0] == version_sum
