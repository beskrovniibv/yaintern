#! /usr/bin/python

# https://contest.yandex.ru/contest/66794/problems/G/

# G. Очередь в ПВЗ*

n, b = map(int, input().split())
seq = list(map(int, input().split()))
ans = 0
q, t = 0, 0
for c in seq:
    ans += min(b, c + q)
    q += c - b
    q = max(q, 0)
    t += q
print(ans + t + q)
