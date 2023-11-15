#! usr/bin/python

# H. Результаты контеста

from math import ceil


class Solution:
    def solve(self, a: int, b: int, n: int) -> bool:
        return a > ceil(b / n)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    n = int(input())
    solution = Solution()
    print("Yes") if solution.solve(a, b, n) else print("No")
