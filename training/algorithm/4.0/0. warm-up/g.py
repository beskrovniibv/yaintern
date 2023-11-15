#! usr/bin/python

# G. Кролик учит геометрию

class Solution:
    def solve(self, n, m, field: list[list[int]]) -> int:
        dp = [[0] * (m + 2) for _ in range(n + 2)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if field[i][j] == 0:
                    dp[i][j] = 0 
                else:
                    if field[i - 1][j - 1] == 1 and field[i - 1][j] == 1 and field[i][j - 1] == 1:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    else:
                        dp[i][j] = 1
        return max(map(max, dp))


if __name__ == '__main__':
    n, m = map(int, input().split())
    field = [[0] * (m + 2) for _ in range(n + 2)]
    for l in range(n):
        field[l + 1] = [0] + list(map(int, input().split())) + [0]
    solver = Solution()
    print(solver.solve(n, m, field))
