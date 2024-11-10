#! /usr/bin/python

# https://contest.yandex.ru/contest/66794/problems/A/

# A. Правильная скобочная последовательность

seq = input()
stack = []
index = 0
for c in seq:
    if c in '([{':
        stack.append(c)
    else:
        if not stack:
            print("no")
            break
        b = stack.pop()
        if ((b == '(' and c != ')')
            or (b == '[' and c != ']') or
            (b == '{' and c != '}')):
            print("no")
            break
else:
    if not stack:
        print("yes")
    else:
        print("no")
