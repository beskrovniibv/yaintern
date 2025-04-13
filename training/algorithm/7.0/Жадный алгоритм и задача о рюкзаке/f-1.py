#! /usr/bin/env python

n, m = map(int, input().split())
mi = [x for x in map(int, input().split())]
ci = [x for x in map(int, input().split())]
w = [[(0, 0, 0)] + [(-1, -1, -1)]*m for _ in range(n + 1)]
for i, (_m, _c) in enumerate(zip(mi, ci)):
    row = i + 1
    for j, value in enumerate(w[i]):
        w[row][j] = value
    for j in range(m - _m, -1, -1):
        if w[row][j] != (-1, -1):
            current = w[row][j + _m][0]
            potential = w[row][j][0] + _c
            if potential > current:
                w[row][j + _m] = (potential, i + 1, w[row][j][2] + _m)
mx, col, row = -1, 0, -1
for i in range(m + 1):
    if w[n][i][0] > mx:
        mx = w[n][i][0]
        col = i
        row = w[n][i][1]
result = []
while mx > 0:
    result.append(w[row][col][1])
    c = ci[w[row][col][1] - 1]
    m = mi[w[row][col][1] - 1]
    mx = mx - c
    col, row = w[row][col][2] - m, w[row][col][1] - 1
for i in result:
    print(i)