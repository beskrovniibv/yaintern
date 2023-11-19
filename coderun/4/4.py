#! usr/bin/python

# 4. Ход конём

moves = [[-1, -2], [-2, -1]]


def main():
    n, m = map(int, input().split())
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            c = 0
            for move in moves:
                y = i + move[0]
                x = j + move[1]
                if (x >= 0 and x < m) and (y >= 0 and y < n):
                    if dp[y][x] == 1:
                        c += 1
                    elif dp[y][x] > 1:
                        c += dp[y][x]
            dp[i][j] = max(c, dp[i][j])
    print(dp[n - 1][m - 1])


if __name__ == '__main__':
    main()
