import heapq
from collections import Counter
from typing import List
from typing import Tuple
from typing import Self

class Container:
    def __init__(self, input_s: str) -> None:
        self.data = input_s
        self.list1: List[int] = []
        self.list2: List[int] = []


    def seed(self) -> None:
        for line in self.data.split("\n"):
            try:
                i1, i2 = line.split()
            except ValueError:
                continue

            heapq.heappush(self.list1, int(i1))
            heapq.heappush(self.list2, int(i2))

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> Tuple[int, int]:
        try:
            return (
                heapq.heappop(self.list1),
                heapq.heappop(self.list2)
            )
        except IndexError:
            raise StopIteration


def part1(input_s: str) -> int:
    c = Container(input_s)
    c.seed()
    ans = 0
    for (i1, i2) in c:
        ans += abs(i1 - i2)
    return ans


def part2(input_s: str) -> int:
    lst1, lst2 = [], []
    for line in input_s.split("\n"):
        try:
            i1, i2 = line.split()
        except ValueError:
            continue
        lst1.append(int(i1))
        lst2.append(int(i2))

    counter = Counter(lst2)
    return sum(i * counter[i] for i in lst1)

