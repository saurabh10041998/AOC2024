import re


PART1_REG = re.compile(r'mul\((?P<num1>\d+),(?P<num2>\d+)\)')


def part1(input_s: str) -> int:
    ans = 0
    matches = re.findall(PART1_REG, input_s)
    for mat in matches:
        ans += int(mat[0]) * int(mat[1])
    return ans
