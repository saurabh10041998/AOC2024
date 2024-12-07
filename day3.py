import re


PART1_REG = re.compile(r'mul\((?P<num1>\d+),(?P<num2>\d+)\)')
PART2_REG = re.compile(r'(mul\((?P<num1>\d+),(?P<num2>\d+)\)|do\(\)|don\'t\(\))')  # noqa:501


def part1(input_s: str) -> int:
    ans = 0
    matches = re.findall(PART1_REG, input_s)
    for mat in matches:
        ans += int(mat[0]) * int(mat[1])
    return ans


def part2(input_s: str) -> int:
    ans = 0
    enabled = True
    for inst, op1, op2 in re.findall(PART2_REG, input_s):
        if inst == "do()":
            enabled = True
        elif inst == "don't()":
            enabled = False
        else:
            if enabled:
                ans += int(op1) * int(op2)
    return ans
