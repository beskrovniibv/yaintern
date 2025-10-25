#! /usr/bin/env python

# H. Премии от начальника*

# https://contest.yandex.ru/contest/80942/problems/H/

n = int(input())
arr = list(map(int, input().split()))
p = [0]*n

for i in range(n):
    p[i] = i + arr[i]
ps = [0]*n
c = [0]*n
_c = [0]*n

for i in range(1, n):
    if i == 0:
        continue
    ps[i] = ps[i - 1] + int((p[i] - i) > i)

for i in range(n):
    l, r = i + 1, p[i]
    if l < n: 
        _c[l] += 1
    if r < n:
        _c[r] -= 1
    # for j in range(l, r):
        # c[j] += 1
q = 0
for i in range(n):
    q += _c[i]
    c[i] += q


result = 0
for i in range(n):
    result += c[i]*arr[i]
print(result)