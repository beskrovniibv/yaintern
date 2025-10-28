#! /usr/bin/env python

# G. Планирование сериала

# https://contest.yandex.ru/contest/80942/problems/G/

# n = int(input())
# s = list(map(int, input().split()))
# a = list(map(int, input().split()))

# p = {}
# idx = set()
# for i in range(n):
#     j = s[i]
#     idx.add(j)
#     p[j] = p.get(j, 0)
#     p[j] += a[i]
# idx = sorted(list(idx))
# mx = 0
# q = 0
# for k, v in p.items():
#     mx += k*v
#     q += v
# mn, result = None, None
# for i in idx:
#     v = abs(mx - i*q)
#     if mn is None and result is None:
#         mn = i
#         result = v
#     elif v < result:
#         mn = i
#         result = v
# print(mn, result)
n = int(input())
s = list(map(int, input().split()))
a = list(map(int, input().split()))

# Объединение и сортировка по s
pairs = sorted(zip(s, a), key=lambda x: x[0])
s_sorted = [x[0] for x in pairs]
a_sorted = [x[1] for x in pairs]

total_weight = sum(a_sorted)
half_weight = total_weight / 2

cumulative = 0
for i in range(n):
    cumulative += a_sorted[i]
    if cumulative >= half_weight:
        e = s_sorted[i]
        break

# Вычисление итоговой суммы
total_cost = 0
for si, ai in zip(s, a):
    total_cost += abs(e - si) * ai

print(e, total_cost)