#! /usr/bin/env python

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        next = self.next.value if self.next else "None"
        return f"{self.value} > {next}"


class RoundQueue():
    def __init__(self):
        self.queue = None
        self.len = 0

    def run(self, value):
        self.len += 1
        node = Node(value)
        if not self.queue:
            self.queue = node
            self.queue.next = self.queue
            return value
        node.next = self.queue
        seek = self.queue
        while seek.next != self.queue:
            seek = seek.next
        seek.next = node
        self.queue = node
        return value

    def move(self, count):
        if self.len == 0:
            return "error"
        if self.len == 1:
            return self.queue.value
        new, prev, last = self.queue, None, self.queue
        for _ in range(count):
            prev = new
            new = new.next
        while last.next != self.queue:
            last = last.next
        if new == self.queue:
            return self.queue.value
        last.next = new
        prev.next = new.next
        new.next = self.queue
        self.queue = new
        return self.queue.value


def main():
    queue = RoundQueue()
    with open(file="input.txt", mode="r", encoding="utf-8") as f:
        n = f.readline()
        i = 0
        for line in f:
            i += 1
            cmd, *args = line.strip().split()
            if cmd.lower() == "run":
                name = ' '.join(args)
                print(queue.run(name))
            else:
                cmd, *args = cmd.split("+")
                if cmd.lower() == "alt":
                    print(queue.move(len(args)))
                else:
                    assert "Error: unknown command"
            if i == n:
                break
    return


if __name__ == "__main__":
    main()
