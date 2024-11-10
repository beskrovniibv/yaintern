#! /usr/bin/python

# https://contest.yandex.ru/contest/66793/problems/D/

# D. Лучший отдых

from collections import deque


def solve(n, k, data):
    deq = []
    idx = 0
    for el in sorted(data):
        if not deq:
            deq.append(el)
            continue
        deq.append(el)
        if abs(el - deq[idx]) > k:
            # deq.pop()
            idx += 1
    return len(deq) - idx


def solve3(n, k, data):
    deq = deque()
    for el in sorted(data):
        if not deq:
            deq.append(el)
            continue
        deq.append(el)
        if abs(el - deq[0]) > k:
            deq.popleft()
    return len(deq)


def solve2(n, m, data):
    if n == 1:
        return 1
    data = sorted(data)
    days = 0
    range = 0
    first = data[0]
    for i in data[1:]:
        if abs(i - first) <= m:
            range += 1
        else:
            range = 0
            first = i
        if range > days:
            days = range
    return days + 1


def debug(solve):
    assert solve(9, 2, [3, 8, 5, 7, 1, 2, 4, 9, 6]) == 3
    assert solve(3, 2, [4, 2, 1]) == 2
    assert solve(3, 0, [1, 3, 1]) == 2
    assert solve(4, 4, [32, 77, 1, 100]) == 1

    print("Well done")


# debug(solve3)
n, k = map(int, input().split())
data = list(map(int, input().split()))
# ans = solve(n, k, data)
# print(ans)
# print("*"*16)
# ans = solve2(n, k, data)
# print(ans)
# print("*"*16)
ans = solve3(n, k, data)
print(ans)
