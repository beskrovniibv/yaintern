#! /usr/bin/env python

# F. Плюсы, минусы и вопросы

# https://contest.yandex.ru/contest/80939/problems/F/

n, m = map(int, input().split())
field, field_ = [], [["*"]*n for _ in range(m)]
rows, cols = {}, {}
for i in range(n):
    s = input()
    rows[i] = (s.count("+") - s.count("-"), s.count("?"))
    field.append(list(s))
for i in range(n):
    for j in range(m):
        field_[j][i] = field[i][j]


# for i in range(n):
#     s = ''.join(field[i])
#     rows[i] = (s.count("+") - s.count("-"), s.count("?"))
for i in range(m):
    s = ''.join(field_[i])
    cols[i] = (s.count("+") - s.count("-"), s.count("?"))

result = None

for i in range(n):
    for j in range(m):
        t = rows[i][0] + rows[i][1] - (cols[j][0] - cols[j][1])
        if field[i][j] == "?":
            t -= 2
        if result is None:
            result = t
            # print(result)
        else:
            if t > result:
                result = t
                # print(result)
print(result)