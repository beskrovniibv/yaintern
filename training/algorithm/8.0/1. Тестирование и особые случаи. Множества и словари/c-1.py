#! /usr/bin/env python

# C. Кибербезопасность

#  https://contest.yandex.ru/contest/80939/problems/C/

from itertools import combinations

s = input()
n = len(s)
d = {}
for c in s:
    d[c] = d.get(c, 0) + 1
r = 1
for p in combinations(d.values(), r=2):
    r += p[0]*p[1]
print(r)