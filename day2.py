import sys
from typing import Tuple
from typing import Type
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

    @classmethod
    def skip_lvl(
        cls: Type['Levels'],
        seq: Sequence[int],
        lvl: int
    ) -> 'Levels':
        return cls(tuple(seq[:lvl]) + tuple(seq[lvl + 1:]))

    @staticmethod
    def _safe_diff(x: int, y: int) -> bool:
        return 1 <= (x - y) <= 3

    def is_safe(self) -> bool:
        typ = self._guess_type()

        if typ == LevelType.FLAT:
            return False

        elif typ == LevelType.INCREASING:
            return all(
                [
                    self._safe_diff(x2, x1) for (x1, x2)
                    in zip(self.seq, self.seq[1:])
                ]
            )

        else:   # LevelType.DECREASING
            return all(
                [
                    self._safe_diff(x1, x2) for (x1, x2)
                    in zip(self.seq, self.seq[1:])
                ]
            )

    def unsafe_at(self) -> Tuple[int, int]:
        assert not self.is_safe()

        typ = self._guess_type()

        if typ == LevelType.FLAT:
            return (0, 1)

        elif typ == LevelType.INCREASING:
            curr_idx = 1
            while curr_idx < len(self.seq):
                prev_idx = curr_idx - 1

                if not self._safe_diff(
                    self.seq[curr_idx],
                    self.seq[prev_idx]
                ):
                    return (prev_idx, curr_idx)

                curr_idx += 1

        else:  # LevelType.DECREASING
            curr_idx = 1
            while curr_idx < len(self.seq):
                prev_idx = curr_idx - 1

                if not self._safe_diff(
                    self.seq[prev_idx],
                    self.seq[curr_idx]
                ):
                    return (prev_idx, curr_idx)

                curr_idx += 1
        raise AssertionError("Should not reach here for unsafe sequence")


def part1(input_s: str) -> int:
    ans = 0
    for line in input_s.split("\n"):
        if line:
            s = Levels(tuple(int(x) for x in line.split()))
            if s.is_safe():
                ans += 1
    return ans


def part2(input_s: str) -> int:
    ans = 0
    for line in input_s.split("\n"):
        if line:
            s = Levels(tuple(int(x) for x in line.split()))

            if s.is_safe():
                ans += 1
            else:
                lv1, lv2 = s.unsafe_at()
                s1 = s.skip_lvl(s.seq, lv1)
                s2 = s.skip_lvl(s.seq, lv2)
                if s1.is_safe() or s2.is_safe():
                    ans += 1
    return ans
