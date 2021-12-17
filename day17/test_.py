from main import *
import pytest


@pytest.mark.parametrize(
    "v0, t, expected",
    [
        (7, 0, 7),
        (7, 1, 6),
        (7, 7, 0),
        (7, 8, 0),
    ],
)
def test_vx(v0, t, expected):
    assert vx(v0, t) == expected


@pytest.mark.parametrize(
    "v0, t, expected",
    [
        (2, 0, 2),
        (2, 1, 1),
        (2, 7, -5),
        (2, 8, -6),
    ],
)
def test_vy(v0, t, expected):
    assert vy(v0, t) == expected


@pytest.mark.parametrize(
    "x0, v0, t, expected",
    [
        (0, 7, 0, 0),
        (0, 7, 1, 7),
        (0, 7, 5, 25),
        (0, 7, 7, 28),
    ],
)
def test_xt(x0, v0, t, expected):
    assert xt(x0, v0, t) == expected


@pytest.mark.parametrize(
    "y0, v0, t, expected",
    [
        (0, 2, 0, 0),
        (0, 2, 1, 2),
        (0, 2, 5, 0),
        (0, 2, 7, -7),
    ],
)
def test_yt(y0, v0, t, expected):
    assert yt(y0, v0, t) == expected


@pytest.mark.parametrize(
    "vx0, vy0, target, expected",
    [
        (7, 2, ((20, 30), (-5, -10)), True),
        (6, 3, ((20, 30), (-5, -10)), True),
        (9, 0, ((20, 30), (-5, -10)), True),
        (17, -4, ((20, 30), (-5, -10)), False),
        (6, 9, ((20, 30), (-5, -10)), True),
    ],
)
def test_hits_target(vx0, vy0, target, expected):
    assert hits_target(vx0, vy0, target)[0] == expected


@pytest.mark.parametrize(
    "target, expected",
    [
        (((20, 30), (-5, -10)), (45, 112)),
    ],
)
def test_throw_with_style(target, expected):
    assert throw_with_style(target, 100, 100) == expected
