#! /usr/bin/python

# https://contest.yandex.ru/contest/66793/problems/C/

# C. Город Че

def solve(n, r, d):
    result = 0
    rigth = 0
    for left in range(n):
        while rigth < n - 1 and d[rigth] - d[left] <= r:
            rigth += 1
        if d[rigth] - d[left] > r:
            result += n - rigth
    return result


n, r = map(int, input().split())
d = list(map(int, input().split()))
ans = solve(n, r, d)
print(ans)
