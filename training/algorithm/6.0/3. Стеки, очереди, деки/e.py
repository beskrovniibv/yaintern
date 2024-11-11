#! /usr/bin/python

# https://contest.yandex.ru/contest/66794/problems/E/

# E. Значение арифметического выражения

from re import search

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a*b

OP = {
    '*': mul,
    '+': sum,
    '-': sub
}

def calc(e):
    st = []
    for c in e:
        if isinstance(c, int):
            st.append(c)
        else:
            if st:
                op2 = st.pop()
            else:
                return None, False
            if st:
                op1 = st.pop()
            else:
                return None, False
            st.append(OP[c](op1, op2))
    return st[0], True

def check(s):
    if search(r'\d+\s+\d+', s):
        return False
    s = s.replace(" ", "")
    if not search(r'^[\d +\-*()]+$', s):
        return False
    if search(r"\([+*]+", s):
        return False
    b = 0
    for c in s:
        if c == "(":
            b += 1
        elif c == ")":
            b -= 1
        if b < 0:
            return False
    else:
        if b != 0:
            return False
    return True

s = input().strip()

if check(s):
    s = s.replace('(', '(0')
    if s[0] != "(":
        s = '0' + s
    s = s.replace(' ', '')
    op = 0
    e = []
    st = []
    n = False
    for ch in s:
        if ch.isdigit():
            op = op*10 + int(ch)
            n = True
        elif ch in "+-":
            if n:
                e.append(op)
                op = 0
                n = False
            while st and st[-1] in "+-*":
                e.append(st.pop())
            st.append(ch)
        elif ch in "*":
            if n:
                e.append(op)
                op = 0
                n = False
            while st and st[-1] in "*":
                e.append(st.pop())
            st.append(ch)
        elif ch == "(":
            st.append(ch)
        elif ch == ")":
            if n:
                e.append(op)
                op = 0
                n = False
            while st and st[-1] != "(":
                e.append(st.pop())
            st.pop()
    if n:
        e.append(op)
        op = 0
        n = False
    while st:
        e.append(st.pop())
    result, fl = calc(e)
    if fl:
        print(result)
    else:
        print("WRONG")
else:
    print("WRONG")
