#! usr/bin/python

# B. Сложить две дроби

from math import gcd
from typing import Tuple


class Solution:
    def solve(self, a: int, b: int, c: int, d: int) -> Tuple[int, int]:
        n = a*d + b*c
        m = b*d
        g = gcd(n, m)
        return (n//g, m//g)


if __name__ == '__main__':
    solution = Solution()
    a, b, c, d = map(int, input().split())
    print(*solution.solve(a, b, c, d))
