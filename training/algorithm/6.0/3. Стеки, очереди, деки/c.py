#! /usr/bin/pyton

# https://contest.yandex.ru/contest/66794/problems/C/

# C. Минимум на отрезке

from collections import deque

st = deque()

n, k = map(int, input().split())
seq = list(map(int, input().split()))

for i, e in enumerate(seq):
    while st and st[-1][0] > e:
        st.pop()
    st.append((e, i))
    if i + 1 >= k:
        print(st[0][0])
    if i >= st[0][1] + k - 1:
        st.popleft()
