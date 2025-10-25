#! /usr/bin/env python

# E. Ремонт выбоин

# https://contest.yandex.ru/contest/80942/problems/E/

n, m, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
_e, e = [0] + [0]*n + [0], [0] + [0]*n + [0]
for _ in range(m):
    v1, v2 = map(int, input().split())
    _e[v1] += 1
    _e[v2 + 1] -= 1
q = 0
for i in range(1, n + 1):
    q += _e[i]
    e[i] += q
s = 0
for i in range(1, n + 1):
    s += a[i]*e[i]
se = [0] + sorted([(e[i], a[i]) for i in range(1, n + 1)], reverse=True)
l = 1
a = 0
while k > 0 and l < n + 1 and s > 0:
    bus_count, pit_count = se[l]
    pit_count = min(pit_count, k)
    a = min(s, bus_count*pit_count)
    k -= pit_count
    s -= a
    l += 1
print(s)