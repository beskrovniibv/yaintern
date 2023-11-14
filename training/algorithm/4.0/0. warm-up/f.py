#! usr/bin/python

# F. Лифт

from math import ceil


class Solution:
    def solve(self, k: int, n: int, a: list[int]) -> int:
        result = 0
        max_floor = 0
        cnt_r = 0
        for i in range(n - 1, -1, -1):
            if a[i] == 0:
                continue
            result += a[i]//k*2*(i + 1)
            cnt_r += a[i] % k
            # if cnt_r == a[i] % k:
            #     max_floor = i + 1
            if a[i] % k:
                max_floor = max_floor if max_floor else i + 1
            if cnt_r >= k:
                cnt_r = cnt_r - k
                # cnt_r = cnt_r % k
                result += 2*(max_floor)
                max_floor = (i + 1) if cnt_r else 0
        if max_floor:
            result += 2*(max_floor)
        return result


if __name__ == '__main__':
    k = int(input())
    n = int(input())
    a = [int(input()) for _ in range(n)]

    solver = Solution()
    print(solver.solve(k, n, a))
