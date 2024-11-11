#! /usr/bin/python

# https://contest.yandex.ru/contest/66794/problems/H/

# H. Стек с суммой*

from collections import deque


class Stack():
    
    def __init__(self):
        self.stack = []
        self.sums = [0]

    
    def append(self, value):
        self.stack.append(value)
        self.sums.append(self.sums[-1] + value)

    def pop(self):
        value = self.stack.pop()
        self.sums.pop()
        return value
    
    def sum(self, count):
        n = len(self.sums)
        result = self.sums[-1] - self.sums[n - count - 1]
        return result

st = Stack()
n = int(input())
for _ in range(n):
    op = input()
    if op[0] == "+":
        st.append(int(op[1:]))
    elif op[0] == "-":
        print(st.pop())
    else:
        print(st.sum(int(op[1:])))
