#! usr/bin/python

# 6. НОП с восстановлением ответа

def main():
    n = int(input())
    nums1 = list(map(int, input().split()))
    m = int(input())
    nums2 = list(map(int, input().split()))
    dp = [[0 for _ in range(n)] for _ in range(m)]
    path = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            if nums1[i] == nums2[j]:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                    if i == 0 and j == 0:
                        path[i][j] = (0, 0)
                    elif i == 0:
                        path[i][j] = (i, j -1)
                    else:
                        path[i][j] = (i - 1, j)
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    path[i][j] = (i - 1, j - 1)
            else:
                if i == 0 or j == 0:
                    if i == 0 and j == 0:
                        pass
                    elif i == 0:
                        dp[i][j] = dp[i][j - 1]
                        path[i][j] = (i, j - 1)
                    else:
                        dp[i][j] = dp[i - 1][j]
                        path[i][j] = (i - 1, j)
                    # dp[i][j] = 0
                else:
                    if dp[i - 1][j] > dp[i][j - 1]:
                        dp[i][j] = dp[i - 1][j]
                        path[i, j] = (i - 1, j)
                    else:
                        dp[i][j] = dp[i][j - 1]
                        path[i][j] = (i, j - 1)
    print(dp[n - 1][m - 1])
    p = []
    i, j = n - 1, m - 1
    while i != 0 or j != 0:
        if path[i][j] == (i - 1, j - 1):
            i -= 1
            j -= 1
            p.append(str(nums1[i]))
        else:
            if path[i][j] == (i - 1, j):
                i -= 1
            else:
                j -= 1
    print(''.join(p[::-1]))

if __name__ == '__main__':
    main()
