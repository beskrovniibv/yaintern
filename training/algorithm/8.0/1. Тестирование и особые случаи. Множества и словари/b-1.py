#! /usr/bin/env python

# B. Мамины поручения

# https://contest.yandex.ru/contest/80939/problems/B/

a, b, c, v0, v1, v2 = map(int, input().split())

w1 = b/v0 + c/v1 + a/v2
w2 = a/v0 + c/v1 + b/v2
w3 = a/v0 + a/v1 + b/v0 + b/v1
w4 = a/v0 + c/v1 + c/v2 + a/v2
w5 = b/v0 + c/v1 + c/v2 + b/v2
w6 = a/v0 + a/v1 + a/v0 + c/v0 + c/v1 + a/v1
w7 = b/v0 + b/v1 + b/v0 + c/v0 + c/v1 + b/v1
w8 = a/v0 + a/v1 + a/v0 + c/v0 + b/v1
w9 = b/v0 + b/v1 + b/v0 + c/v0 + a/v1
w10 = a/v0 + c/v0 + c/v1 + a/v2
w11 = b/v0 + c/v0 + c/v1 + b/v2
print(min(w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11))