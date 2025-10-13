#! /usr/bin/env python

# F. Сбор монеток

# https://contest.yandex.ru/contest/80940/problems/F/

from copy import copy

row_count = int(input())
field = [list(input()) for _ in range(row_count)]
edp = [[0, 0, 0] for _ in range(row_count)]
result = [0, 0, 0]
for s in (0, 1, 2):
    dp = copy(edp)
    tresult = 0
    if field[0][s] == 'W':
        continue
    for r in range(row_count):
        t = 0
        if r == 0 and field[0][s] == "C":
            dp[0][s] = 1
            tresult = 1
        elif r > 0:
            stop = True
            for i in (0, 1, 2):
                if field[r][i] == "W":
                    continue
                if i == 0:
                    dp[r][i] = max(
                        -1 if (field[r - 1][i] == "W" or dp[r - 1][i] == -1) else (dp[r - 1][i] + (1 if field[r][i] == "C" else 0)),
                        -1 if (field[r - 1][i + 1] == "W" or dp[r - 1][i + 1] == -1) else (dp[r - 1][i + 1] + (1 if field[r][i] == "C" else 0)),
                    )
                    stop = stop and field[r - 1][i] == "W" and field[r - 1][i + 1] == "W"
                elif i == 1:
                    dp[r][i] = max(
                        -1 if field[r - 1][i - 1] == "W" or dp[r - 1][i - 1] == -1 else (dp[r - 1][i - 1] + (1 if field[r][i] == "C" else 0)),
                        -1 if field[r - 1][i] == "W" or dp[r - 1][i] == -1 else (dp[r - 1][i] + (1 if field[r][i] == "C" else 0)),
                        -1 if field[r - 1][i + 1] == "W" or dp[r - 1][i + 1] == -1 else (dp[r - 1][i + 1] + (1 if field[r][i] == "C" else 0)),
                    )
                    stop = stop and field[r - 1][i] == "W" and field[r - 1][i + 1] == "W" and field[r - 1][i - 1] == "W"
                elif i == 2:
                    dp[r][i] = max(
                        -1 if field[r - 1][i] == "W" or dp[r - 1][i] == -1 else (dp[r - 1][i] + (1 if field[r][i] == "C" else 0)),
                        -1 if field[r - 1][i - 1] == "W" or dp[r - 1][i - 1] == -1 else (dp[r - 1][i - 1] + (1 if field[r][i] == "C" else 0)),
                    )
                    stop = stop and field[r - 1][i] == "W" and field[r - 1][i - 1] == "W"
                # stop = stop and stop
                t = max(
                    t,
                    dp[r][i]
                )
            tresult = max(
                tresult,
                t
            )
            if stop:
                break
    result[s] = tresult

for r in dp:
    print(*r)
print(max(result))