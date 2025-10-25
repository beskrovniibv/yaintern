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

for i in range(1, n):
    if i == 0:
        continue
    ps[i] = ps[i - 1] + int((p[i] - i) > i)
for i in range(n):
    v = 0
    for j in range(0, i):
        if p[j] > i:
            v += 1
    c[i] = v
result = 0
for i in range(n):
    result += c[i]*arr[i]
print(result)