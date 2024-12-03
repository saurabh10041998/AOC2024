import pytest
from pathlib import Path
from day2 import part1
from day2 import part2
from day2 import Levels
from day2 import LevelType


@pytest.mark.parametrize(
    ("input_l", "expected"),
    (
        ((1, 2, 3, 4, 5), LevelType.INCREASING),
        ((4, 3, 2, 1, 1), LevelType.DECREASING),
        ((1, 1, 2, 4, 5), LevelType.FLAT),
    )
)
def test_sequence_guessing_type(input_l, expected):
    s = Levels(input_l)
    assert s._guess_type() == expected


@pytest.mark.parametrize(
    ("input_l", "expected"),
    (
        ((-1, -2), True),
        ((2, 3), False),
        ((4, 7), False),
        ((3, 2), True)
    )
)
def test_safe_diff(input_l, expected):
    assert Levels._safe_diff(input_l[0], input_l[1]) == expected


@pytest.mark.parametrize(
    ("input_l", "expected"),
    (
        ((7, 6, 4, 2, 1), True),
        ((1, 2, 7, 8, 9), False),
        ((9, 7, 6, 2, 1), False),
        ((1, 3, 2, 4, 5), False),
        ((8, 6, 4, 4, 1), False),
        ((1, 3, 6, 7, 9), True),
    )
)
def test_safe_sequence(input_l, expected):
    s = Levels(input_l)
    assert s.is_safe() == expected


def test_part1_min():
    input_s = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
    assert part1(input_s) == 2


def test_part1():
    input_f = Path(__file__).parent / "data" / "day2.txt"
    with open(input_f, 'r') as f:
        input_s = f.read()
    assert part1(input_s) == 663


@pytest.mark.parametrize(
    ("input_l", "lvl", "expected"),
    (
        ((1, 2, 7, 8, 9), 1, (1, 7, 8, 9)),
        ((1, 2, 7, 8, 9), 2, (1, 2, 8, 9)),
        ((9, 7, 6, 2, 1), 2, (9, 7, 2, 1)),
        ((9, 7, 6, 2, 1), 3, (9, 7, 6, 1)),
        ((1, 3, 2, 4, 5), 1, (1, 2, 4, 5)),
        ((1, 3, 2, 4, 5), 2, (1, 3, 4, 5)),
        ((8, 6, 4, 4, 1), 2, (8, 6, 4, 1)),
        ((8, 6, 4, 4, 1), 3, (8, 6, 4, 1)),
    )
)
def test_skip_lvl(input_l, lvl, expected):
    s = Levels(input_l)
    new_s = s.skip_lvl(s.seq, lvl)
    new_s.seq == expected


def test_part2_min():
    input_s = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
    assert part2(input_s) == 4


def test_part2():
    input_f = Path(__file__).parent / "data" / "day2.txt"
    with open(input_f, 'r') as f:
        input_s = f.read()
    assert part2(input_s) == 692
