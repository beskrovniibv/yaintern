#! /usr/bin/python

# https://contest.yandex.ru/contest/66794/problems/D/

# D. Постфиксная запись

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a*b

op = {
    '*': mul,
    '+': sum,
    '-': sub
}


st = []
seq = list(input().split())
for c in seq:
    if c.isdigit():
        st.append(int(c))
    else:
        op2 = st.pop()
        op1 = st.pop()
        st.append(op[c](op1, op2))

print(st[0])
