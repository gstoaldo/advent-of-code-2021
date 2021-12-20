from main import *
import pytest


def test_add_margin():
    sample = [["#"]]
    expected = [
        [".", ".", "."],
        [".", "#", "."],
        [".", ".", "."],
    ]
    assert add_margin(sample, 1) == expected
    assert add_margin(sample, 0) == sample


def test_square():
    sample = [
        ["#", "#", "#"],
        ["#", ".", "#"],
        ["#", "#", "#"],
    ]
    assert square(sample, 0, 0) == "....##.#."
    assert square(sample, 1, 1) == "####.####"


def test_pixels_to_decimal():
    assert pixels_to_decimal("...#...#.") == 34


def test_part1():
    alg, img = parse("example.txt")
    img = add_margin(img, 5)
    img = enhance(img, alg)
    assert count_light_pixels(img) == 24
    img = enhance(img, alg)
    assert count_light_pixels(img) == 35


def test_part2():
    alg, img = parse("example.txt")
    img = process(img, alg, 50)
    assert count_light_pixels(img) == 3351
