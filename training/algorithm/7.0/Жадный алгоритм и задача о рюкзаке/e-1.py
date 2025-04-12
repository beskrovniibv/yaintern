#! /usr/bin/env python

n, m = map(int, input().split())
mi = [x for x in map(int, input().split())]
ci = [x for x in map(int, input().split())]
w = [0] + [-1]*m
for _m, _c in zip(mi, ci):
    for i in range(m - _m, -1, -1):
        if w[i] != -1:
            w[i + _m] = max(w[i] + _c, w[i + _m])
i = w[0]
for _w in w:
    if _w > i:
        i = _w
print(i)
