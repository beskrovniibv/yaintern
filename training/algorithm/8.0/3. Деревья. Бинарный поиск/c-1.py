#! /usr/bin/env python

# C. Рекламное объявление

# https://contest.yandex.ru/contest/80941/problems/C/

"""
1.400000000000199973
3 10 7
4 3
3 2
4 2

0.333333333333666715
2 10 1
2 1
3 2
"""

from bisect import bisect_left as bisect
from operator import mul


def is_allright(words, k, w, h):
    current_width, current_height = 0, 0
    words_in_line = 0
    line_width = 0
    i = 0
    while i < len(words):
        _w, _h = map(lambda x: x*k, words[i])
        if words_in_line == 0 or words[i - 1][1] != words[i][1]:
            if words_in_line != 0:
                current_width = max(current_width, line_width)
                words_in_line = 0
                line_width = 0
            current_height += _h
            line_width += _w
            words_in_line += 1
        else:
            line_width += _w
            words_in_line += 1
        if line_width <= w:
            i += 1
        elif line_width > w:
            if words_in_line > 1:
                line_width -= _w
                words_in_line = 0
                current_width = max(current_width, line_width)
                line_width = 0
            else:
                words_in_line = 0
                current_width = max(current_width, line_width)
                line_width = 0
                i += 1
    current_width = max(current_width, line_width)
    return current_width, current_height


n, W, H = map(int, input().split())
words = [tuple(map(int, input().split())) for _ in range(n)]
msg = []
mxw, mxh = 0, 0
for w, h in words:
    if w > mxw:
        mxw = w
    if h > mxh:
        mxh = h
    if msg:
        if h != msg[-1][-1][1]:
            if h + msg[-1][-1][1] > mxh:
                mxh = h + msg[-1][-1][1]
            msg.append([(w, h)])
        else:
            msg[-1].append((w, h))
    else:
        msg.append([(w, h)])
k_max = max(
    W/mxw,
    H/mxh
)
# print(words)
# print(msg)
# print(mxw, mxh)
# print(k_max)
l, r = 0, k_max
while abs(r - l) > 10**-6:
    m = l + (r - l)/2
    kw, kh = is_allright(words, m, W, H)
    if kw > W or kh > H:
        r = m
    else:
        l = m
print(l)