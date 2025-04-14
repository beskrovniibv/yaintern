#! /usr/bin/env python

from functools import lru_cache


MAX = 2**32 + 1

m = int(input())
a = [(2**i, x, (2**i)/x) for i, x in enumerate(map(int, input().split()))]
n = len(a)
mn = a[0][2]
for i in range(n):
    e = a[i]
    if e[2] > mn:
        a[i] = (e[0], a[i - 1][1]*2, a[i - 1][2])
    elif e[2] < mn:
        mn = e[2]
# a.sort(key=lambda a: a[1])

def foo(value, price):
    if value == 0:
        return True
    w, i = 0, 30
    while price > 0 and i >= 0:
        while a[i][0] <= price:
            w += a[i][1]
            price -= a[i][0]
            if w >= value:
                return True
        i -= 1
    return False


left, right = 0, MAX
while left < right:
    mid = (left + right) // 2
    if not foo(m, mid):
        left = mid + 1
    else:
        right = mid
print(left)
