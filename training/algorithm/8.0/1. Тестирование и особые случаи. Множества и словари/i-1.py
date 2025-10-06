#! /usr/bin/env python

# I. Новые ПДД*

# https://contest.yandex.ru/contest/80939/problems/I/

x0, y0 = map(int, input().split())
x1, y1 = map(int, input().split())

if x1 == x0 and y1 == y0:
    print(0)
elif y1 == y0:  # x1 != x0
    distance = abs(x1 - x0) - 1
    print(distance*3)
elif x1 == x0:  # y1 != y0
    distance = abs(y1 - y0) - 1
    print(distance*3)
else:           # x1 != x0 and y1 != y0
    dx = abs(x1 - x0) - 1
    dy = abs(y1 - y0) - 1
    print(dx*3 + dy*3 + 1)