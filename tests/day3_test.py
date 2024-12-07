from pathlib import Path
from day3 import part1
from day3 import part2


def test_part1_min():
    input_s = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
    assert part1(input_s) == 161


def test_part1():
    input_f = Path(__file__).parent / "data" / "day3.txt"
    with open(input_f, 'r') as f:
        input_s = f.read()
    assert part1(input_s) == 164730528


def test_part2_min():
    input_s = """\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""
    assert part2(input_s) == 48


def test_part2():
    input_f = Path(__file__).parent / "data" / "day3.txt"
    with open(input_f, 'r') as f:
        input_s = f.read()
    assert part2(input_s) == 70478672
