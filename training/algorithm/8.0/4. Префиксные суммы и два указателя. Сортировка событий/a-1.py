#! /usr/bin/env python

# A. Рейсы между офисами

# https://contest.yandex.ru/contest/80942/problems/A/

def key(x):
    return (x[0], x[1], -x[2])

n = int(input())
N = []
for _ in range(n):
    b, e = input().split('-')
    h1, m1 = map(int, b.split(":"))
    h2, m2 = map(int, e.split(":"))
    N.append((h1, m1, -1, 1))
    N.append((h2, m2, 1, 1))
m = int(input())
M = []
for _ in range(m):
    b, e = input().split('-')
    h1, m1 = map(int, b.split(":"))
    h2, m2 = map(int, e.split(":"))
    M.append((h1, m1, -1, 2))
    M.append((h2, m2, 1, 2))
ALL = N + M
ALL.sort(key=key)
c = 0
mx = 0
q1, q2 = 0, 0
for e in ALL:
    if e[2] == 1:  # окончили рейс
        if e[3] == 1:
            q2 += 1
        else:
            q1 += 1
    else:  # должны начать рейс
        if e[3] == 1:  # из офиса 1
            if q1 == 0:
                mx += 1
            else:
                q1 -= 1
        else:
            if q2 == 0:
                mx += 1
            else:
                q2 -= 1
print(mx)