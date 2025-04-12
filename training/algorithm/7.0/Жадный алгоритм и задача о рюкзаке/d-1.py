#! /usr/bin/env python

n, m = map(int, input().split())
mi = [x for x in map(int, input().split())]
w = [False]*(m + 1)
w[0] = True
for e in mi:
    for i in range(m - e, -1, -1):
        if w[i]:
            w[i + e] = True
i = m
while not w[i]:
    i -= 1
print(i)