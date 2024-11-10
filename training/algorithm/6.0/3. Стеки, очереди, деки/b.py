#! /usr/bin/python

# https://contest.yandex.ru/contest/66794/problems/B/

# B. Великое Лайнландское переселение

n = int(input())
a = list(map(int, input().split()))
result = [0] * n
st = []
for i, e in enumerate(a):
    f = False
    while st and st[-1][0] > e:
        _, j = st.pop()
        result[j] = i
    st.append((e, i))
while st:
    result[st[-1][1]] = -1
    st.pop()
print(*result)
