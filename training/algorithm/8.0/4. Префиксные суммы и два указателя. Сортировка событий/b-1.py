#! /usr/bin/env python

# B. Транспортные налоги

# https://contest.yandex.ru/contest/80942/problems/B/

from bisect import bisect_left

n = int(input())
taxes = [tuple(map(int, input().split())) for _ in range(n)]
taxes.sort()
m = int(input())
result = [None]*m
for i in range(m):
    q = int(input())
    j = bisect_left(taxes, q, key=lambda x: x[0])
    b, t = taxes[j] if j < n else taxes[-1]
    if b >= q and j > 0:
        b, t = taxes[j - 1]
    result[i] = t*q
print(*result, sep="\n")