import sys
from typing import Sequence
from enum import Enum


class LevelType(Enum):
    FLAT = 0
    INCREASING = 1
    DECREASING = 2


class Levels:
    def __init__(self, seq: Sequence[int]) -> None:
        self.seq = seq

    def _guess_type(self) -> LevelType:
        try:
            assert len(self.seq) >= 2
        except AssertionError:
            print(
                f"{self.seq=} does not look like length 2 seq",
                file=sys.stderr
            )
            return LevelType.FLAT

        if self.seq[0] < self.seq[1]:
            return LevelType.INCREASING
        elif self.seq[0] > self.seq[1]:
            return LevelType.DECREASING
        else:
            return LevelType.FLAT

    @staticmethod
    def _safe_diff(x: int, y: int) -> bool:
        return 1 <= (x - y) <= 3

    def is_safe(self) -> bool:
        typ = self._guess_type()
        match typ:
            case LevelType.FLAT:
                return False
            case _:
                if typ == LevelType.INCREASING:
                    return all(
                        [
                            self._safe_diff(x2, x1) for (x1, x2)
                            in zip(self.seq, self.seq[1:])
                        ]
                    )
                else:  # LevelType.DECREASING
                    return all(
                        [
                            self._safe_diff(x1, x2) for (x1, x2)
                            in zip(self.seq, self.seq[1:])
                        ]
                    )
        raise NotImplementedError(f"Not implemented for {self.seq=}")


def part1(input_s: str) -> int:
    ans = 0
    for line in input_s.split("\n"):
        if line:
            s = Levels(tuple(int(x) for x in line.split()))
            if s.is_safe():
                ans += 1
    return ans
