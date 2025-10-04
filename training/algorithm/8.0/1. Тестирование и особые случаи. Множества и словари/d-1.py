#! /usr/bin/env python

# D. Отборочный контест

# https://contest.yandex.ru/contest/80939/problems/D/

n, k = map(int, input().split())
topics = list(map(int, input().split()))
d = {}
result1 = []
result2 = []
for i in range(n):
    d[topics[i]] = d.get(topics[i], [])
    d[topics[i]].append(topics[i])
for _, v in d.items():
    result1.append(v[0])
    result2 += v[1:]
print(*(result1 + result2)[:k])