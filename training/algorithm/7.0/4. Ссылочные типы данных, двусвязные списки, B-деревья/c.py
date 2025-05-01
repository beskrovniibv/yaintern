#! /usr/bin/env python

# C. Дек с защитой от ошибок

from sys import exit


class Node():
    def __init__(self, value):
        self.value = value
        self.prev, self.next = None, None


class Deque():
    def __init__(self):
        self.len = 0
        self.deque = None

    def push_front(self, value):
        node = Node(value)
        if self.len == 0:
            self.deque = node
        else:
            node.next = self.deque
            self.deque = node
        self.len += 1
        return "ok"

    def push_back(self, value):
        node = Node(value)
        if self.len == 0:
            self.deque = node
        else:
            seek = self.deque
            while seek.next:
                seek = seek.next
            seek.next = node
        self.len += 1
        return "ok"

    def pop_front(self):
        if self.len == 0:
            return "error"
        node = self.deque
        self.deque = node.next
        self.len -= 1
        return node.value

    def pop_back(self):
        if self.len == 0:
            return "error"
        seek, prev = self.deque, None
        while seek.next:
            prev = seek
            seek = seek.next
        node = seek
        prev.next = None
        self.len -= 1
        return node.value

    def front(self):
        if self.len == 0:
            return "error"
        return self.deque.value

    def back(self):
        if self.len == 0:
            return "error"
        seek = self.deque
        while seek.next:
            seek = seek.next
        return seek.value

    def size(self):
        return self.len

    def clear(self):
        self.len = 0
        self.deque = None
        return "ok"


def main():
    deque = Deque()
    with open(file="input.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            cmd, *args = line.strip().split()
            if cmd == "push_front":
                print(deque.push_front(args[0]))
            elif cmd == "push_back":
                print(deque.push_back(args[0]))
            elif cmd == "pop_front":
                print(deque.pop_front())
            elif cmd == "pop_back":
                print(deque.pop_back())
            elif cmd == "front":
                print(deque.front())
            elif cmd == "back":
                print(deque.back())
            elif cmd == "size":
                print(deque.size())
            elif cmd == "clear":
                print(deque.clear())
            elif cmd == "exit":
                print("bye")
                exit()
            else:
                assert "error: unknown command"


if __name__ == "__main__":
    main()
