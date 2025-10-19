#! /usr/bin/env python

# A. Полка раздора

# https://contest.yandex.ru/contest/80941/problems/A/

a, b, S = map(int, input().split())
D = (b + a)**2 - 4*(a*b - S)
if D**0.5 == int(D**0.5):
    d1 = int(D**0.5)
    d2 = -d1
    x1 = ((b + a) + d1)/2
    x2 = ((b + a) + d2)/2
    s = False
    if x1 > 0 and x1 == int(x1) and x1 > a and x1 > b:
        print(int(x1))
        s = True
    if x2 > 0 and x2 == int(x2) and x1 > a and x2 > b:
        print(int(x2))
        s = True
    if not s:
        print(-1)
else:
    print(-1)