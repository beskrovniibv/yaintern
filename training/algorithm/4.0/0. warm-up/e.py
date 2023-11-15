#! usr/bin/python

# E. Средний уровень


class Solution:
    def solve(self, n: int, values: list[int]) -> list[int]:
        result = [0] * n
        pref_sum = [0] * (n + 1)
        for i, v in enumerate(values):
            pref_sum[i + 1] = v if i == 0 else v + pref_sum[i]
        for i, v in enumerate(values):
            l = i + 1
            r = n
            left = pref_sum[l - 1]
            rigth = pref_sum[r] - left
            result[i] = rigth - v * (r - l + 1) + (v * (l - 1) - left)
        return result


if __name__ == '__main__':
    n = int(input())
    values = list(map(int, input().split()))
    # n = 5
    # values = [3, 7, 8, 10, 15]
    solve = Solution()
    print(*solve.solve(n, values))
