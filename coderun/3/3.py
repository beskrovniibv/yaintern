#! usr/bin/python

# 3. Вывести маршрут максимальной стоимости

def main():
    n, m = map(int, input().split())
    array = [[]] * n
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        array[i] = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            if i == 0:
                if j == 0:
                    dp[i][j] = array[i][j]
                else:
                    dp[i][j] = dp[i][j - 1] + array[i][j]
            else:
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + array[i][j]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + array[i][j]
    # print(dp[n - 1][m - 1])
    path = []
    i, j = n - 1, m - 1
    while i != 0 or j != 0:
        if dp[i][j] == dp[i - 1][j] + array[i][j]:
            path.append('D')
            i -= 1
        else:
            path.append('R')
            j -= 1
    print(dp[n - 1][m - 1])
    print(' '.join(path[::-1]))


if __name__ == '__main__':
    main()
