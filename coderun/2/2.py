#! usr/bin/python

# 2. Самый дешевый путь

def main():
    n, m = map(int, input().split())
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    array = [0] * n
    for i in range(n):
        row = list(map(int, input().split()))
        array[i] = list(row)
    for i in range(n):
        for j in range(m):
            if i == 0:
                if j == 0:
                    dp[i + 1][j + 1] = array[i][j]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j] + array[i][j]
            else:
                if j == 0:
                    dp[i + 1][j + 1] = dp[i][j + 1] + array[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1] + array[i][j], dp[i + 1][j] + array[i][j])
    print(dp[n][m])


if __name__ == '__main__':
    main()
