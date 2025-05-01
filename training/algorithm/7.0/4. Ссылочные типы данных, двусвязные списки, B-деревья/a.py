#! /usr/bin/env python

# A. Стек с защитой от ошибок

from sys import exit


class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Stack():
    def __init__(self):
        self.stack = None
        self.len = 0

    def push(self, value):
        node = Node(value)
        if self.len == 0:
            self.stack = node
        else:
            seek = self.stack
            while seek.next:
                seek = seek.next
            seek.next = node
        self.len += 1
        return "ok"

    def pop(self):
        if self.len == 0:
            return 'error'
        seek, prev = self.stack, None
        while seek.next:
            prev = seek
            seek = seek.next
        self.len -= 1
        if self.len == 0:
            self.stack = None
        else:
            prev.next = None
        return seek.value

    def back(self):
        if self.len == 0:
            return 'error'
        seek = self.stack
        while seek.next:
            seek = seek.next
        return seek.value

    def size(self):
        return self.len

    def clear(self):
        self.len = 0
        self.stack = None
        return "ok"


def argparse(stack, args):
    cmd, *args = args.split()
    if cmd == "exit":
        print("bye")
        exit()
    elif cmd == "push":
        print(stack.push(args[0]))
    elif cmd == "pop":
        print(stack.pop())
    elif cmd == "back":
        print(stack.back())
    elif cmd == "size":
        print(stack.size())
    elif cmd == "clear":
        print(stack.clear())
    else:
        assert "Error: unknown command"


def main():
    stack = Stack()
    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            argparse(stack, line.strip())


if __name__ == "__main__":
    main()
