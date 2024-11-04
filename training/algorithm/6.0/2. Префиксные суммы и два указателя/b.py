#! /usr/bin/python

# https://contest.yandex.ru/contest/66793/problems/B/

# B. Сумма номеров

def solve(arr, k):
    p = [0] * (len(arr) + 1)
    for i, v in enumerate(arr):
        p[i + 1] = p[i] + v
    l, r = 0, 1
    result = 0
    for l in range(len(p)):
        while r < len(arr) and p[r] - p[l] < k:
            r += 1
        if p[r] - p[l] == k:
            result += 1
    return result

n, k = map(int, input().split())
data = list(map(int, input().split()))
print(solve(data, k))
