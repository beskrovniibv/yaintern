#! /usr/bin/env python

# G. Пять подряд

# https://contest.yandex.ru/contest/80939/problems/G/

D = (
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
)
count = 0
n, m = map(int, input().split())
f = []
for _ in range(n):
    f.append(list(input()))
for i in range(n):
    for j in range(m):
        c = f[i][j]
        if c == '.':
            continue
        for d in D:
            dx, dy = d
            x, y = j, i
            x1, y1 = x + dx, y + dy
            if (x1 >= m or x1 < 0) or (y1 >= n):
                continue
            count = 1
            while f[y1][x1] == c:
                count += 1
                if count == 5:
                    break
                x1, y1 = x1 + dx, y1 + dy
                if (x1 >= m or x1 < 0) or (y1 >= n):
                    break
            if count == 5:
                break
        if count == 5:
            break
    if count == 5:
        break
print(('No', 'Yes')[count == 5])