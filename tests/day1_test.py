from day1 import part1
from day1 import part2
from day1 import Container
from pathlib import Path


def test_container():
    data_s = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""
    c = Container(data_s)
    c.seed()
    lst = []
    for item in c:
        lst.append(item)

    assert lst == [
        (1, 3),
        (2, 3),
        (3, 3),
        (3, 4),
        (3, 5),
        (4, 9),
    ]


def test_part1_min():
    input_s = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""
    assert part1(input_s) == 11


def test_part1():
   input_f = Path(__file__).parent / "data" / "day1.txt"
   with open(input_f, 'r') as f:
       input_s = f.read()

   assert part1(input_s) == 1197984


def test_part2_min():
    input_s = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""
    assert part2(input_s) == 31


def test_part2():
    input_f  = Path(__file__).parent / "data" / "day1.txt"
    with open(input_f, 'r') as f:
        input_s = f.read()

    assert part2(input_s) == 23387399

