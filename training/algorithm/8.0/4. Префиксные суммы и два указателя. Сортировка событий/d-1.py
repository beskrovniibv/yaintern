#! /usr/bin/env python

# D. Победила Дружба

# https://contest.yandex.ru/contest/80942/problems/D/

n = int(input())

q = [0] + list(map(int, input().split()))
s1 = [0] + [0]*n
s2 = [0] + [0]*n

for i in range(1, n):
    s1[i] = s1[i - 1] + q[i]
for i in range(n - 1, 0, -1):
    s2[i] = s2[i + 1] + q[i + 1]
mn, fl, fr = abs(q[1] - q[-1]), 1, n
l, r = 1, n - 1
while l <= r:
    d = abs(s1[l] - s2[r])
    if d < mn:
        mn = d
        fl = l
        fr = r + 1
    _p1 = abs(s1[l + 1] - s2[r])
    _p2 = abs(s1[l] - s2[r - 1])
    if _p1 < _p2:
        l += 1
    else:
        r -= 1
print(mn, fl, fr)