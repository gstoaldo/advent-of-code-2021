import pytest
from main import *


@pytest.mark.parametrize(
    "line, illegal_char",
    [
        ("()", None),
        ("([)]", ")"),
        ("(([]))", None),
        ("{([(<{}[<>[]}>{[]{[(<()>", "}"),
        ("[[<[([]))<([[{}[[()]]]", ")"),
        ("<{([([[(<>()){}]>(<<{{", ">"),
    ],
)
def test_find_first_illegal_char(line, illegal_char):
    assert find_first_illegal_char(line) == illegal_char


def test_part1():
    input = parse("example.txt")
    assert syntax_error_score(input) == 26397
