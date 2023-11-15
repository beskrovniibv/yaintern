#! usr/bin/python

# F. Лифт

from math import ceil


class Solution:
    def solve(self, k: int, n: int, a: list[int]) -> int:
        result = 0
        v = 0
        for i in range(n - 1, -1, -1):
            if a[i] == 0:
                continue
            p = k - a[i] % k
            if 
            t = 2*(i + 1)
            result += c*t
        return result


if __name__ == '__main__':
    k = int(input())
    n = int(input())
    a = [int(input()) for _ in range(n)]

    solver = Solution()
    print(solver.solve(k, n, a))
