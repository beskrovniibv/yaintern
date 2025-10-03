#! /usr/bin/env python

# A. Делёж грибов

#  https://contest.yandex.ru/contest/80939/problems/A/

n, a = int(input()), list(map(int, input().split()))
v, m = [], []
mnv, mxm = 1001, -1
sv, sm = 0, 0
for i, e in enumerate(a):
    if i & 1 == 0:
        v.append(e)
        if e < mnv:
            mnv = e
        sv += e
    else:
        m.append(e)
        if e > mxm:
            mxm = e
        sm += e
if mnv < mxm:
    sv = sv - mnv + mxm
    sm = sm - mxm + mnv
print(sv - sm)