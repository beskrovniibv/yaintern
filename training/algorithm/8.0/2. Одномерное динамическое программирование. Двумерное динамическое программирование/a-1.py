#! /usr/bin/env python

# A. Мячик на лесенке

# https://contest.yandex.ru/contest/80940/problems/

n = int(input())
a = [1] + [-1]*n
for i in range(1, n + 1):
    for j in (1, 2, 3):
        c = i - j
        if c >= 0:
            if a[c] >= 0:
                a[i] = max(a[c], a[i] + a[c])
print(a[-1])