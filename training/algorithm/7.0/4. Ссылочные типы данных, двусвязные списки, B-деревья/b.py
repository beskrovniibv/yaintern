#! /usr/bin/env python

# B. Очередь с защитой от ошибок

from sys import exit


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue():
    def __init__(self):
        self.queue = None
        self.len = 0

    def push(self, value):
        node = Node(value)
        if self.len == 0:
            self.queue = node
        else:
            seek = self.queue
            while seek.next:
                seek = seek.next
            seek.next = node
        self.len += 1
        return "ok"

    def pop(self):
        if self.len == 0:
            return "error"
        node = self.queue
        self.queue = node.next
        self.len -= 1
        if self.len == 0:
            self.queue = None
        return node.value

    def front(self):
        if self.len == 0:
            return "error"
        return self.queue.value

    def size(self):
        return self.len

    def clear(self):
        self.len = 0
        self.queue = None
        return "ok"


def main():
    queue = Queue()
    with open("input.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            cmd, *args = line.strip().split()
            if cmd == "exit":
                print("bye")
                exit()
            elif cmd == "push":
                print(queue.push(args[0]))
            elif cmd == "pop":
                print(queue.pop())
            elif cmd == "front":
                print(queue.front())
            elif cmd == "size":
                print(queue.size())
            elif cmd == "clear":
                print(queue.clear())
            else:
                assert "Error: unknown command"


if __name__ == "__main__":
    main()
