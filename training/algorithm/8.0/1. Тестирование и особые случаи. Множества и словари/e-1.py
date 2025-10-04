#! /usr/bin/env python

# E. Табло с инкрементом

# https://contest.yandex.ru/contest/80939/problems/E/

import random

Q = {
    0:  (0, [0], [0]),
    1:  ([2, 4, 8, 6]),
    2:  ([4, 8, 6, 2]),
    3:  ([6, 2, 4, 8]),
    4:  ([8, 6, 2, 4]),
    5: ([0]),
    6: ([2, 4, 8, 6]),
    7: ([4, 8, 6, 2]),
    8: ([6, 2, 4, 8]),
    9: ([8, 6, 2, 4]),
}


def sum0(n, k):
    for i in range(k):
        n += n % 10
    return n


def sum1(n, k):
    e = n % 10
    if e == 0 or k == 0:
        return n
    if e == 5:
        return n + 5
    z = n//10*10 + (10 if e >= 5 else 0)
    a = Q[e][0]
    b = ((k - 1)//4)*20
    c = sum(Q[e][:(k - 1) % 4])
    return z + a + b + c

# n, k = map(int, input().split())
# print(sum1(n, k))
# print(sum0(n, k))

n, k = map(int, input().split())
for k in range(1, k + 1):
    s1 = sum1(n, k)
    s0 = sum0(n, k)
    print(f"{s1}:{s0}")
    if s1 != s0:
        print(f"failed at ({n}, {k})")
else:
    print("ok")


# n = random.randint(0, 10**9)
# k = random.randint(0, 10**9)
# print(f"n = {n}, k = {k}: {sum1(n, k)}, {sum0(n, k)}")