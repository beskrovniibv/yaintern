#! /usr/bin/python

# https://contest.yandex.ru/contest/66793/problems/

# A. Префиксные суммы

n = int(input())
data = list(map(int, input().split()))
prefix = [0] * (n + 1)
c = 0
for i, v in enumerate(data):
    prefix[i + 1] = prefix[i] + v
print(*prefix[1:])