#! /usr/bin/env python

class Node():
    def __init__(self, value):
        self.value = value
        self.prev, self.next = None, None

    def __repr__(self):
        prev = self.prev.value if self.prev else "None"
        next = self.next.value if self.next else "None"
        return f"[{prev}] > [{self.value}] > [{next}]"


class Chain():
    def __init__(self, data):
        self.len = 0
        self.chain = None
        self.data = data
        self.result = [0]*len(self.data)
        for index, value in enumerate(self.data):
            self.add(index, value)

    def add(self, index, value):
        node = Node((index, value))
        if self.len == 0:
            self.chain = node
            self.chain.next = self.chain
            self.chain.prev = self.chain
        else:
            last = self.chain
            while last.next != self.chain:
                last = last.next
            last.next = node
            node.next = self.chain
            node.prev = last
            self.chain.prev = node
        self.len += 1

    def delete(self, node):
        last = self.chain
        for _ in range(self.len):
            if last == node:
                last.prev.next = last.next
                last.next.prev = last.prev
                self.len -= 1
                if last == self.chain:
                    self.chain = last.next
                break
            last = last.next

    def round(self, round):
        if self.len <= 2:
            return False
        candidate = []
        last = self.chain
        for _ in range(self.len):
            if last.value[1] < last.prev.value[1] and last.value[1] < last.next.value[1]:
                candidate.append(last)
            last = last.next
        for c in candidate:
            self.delete(c)
            self.result[c.value[0]] = round
        return bool(candidate) and self.len >= 2

    def __repr__(self):
        elems = []
        last = self.chain
        while last.next != self.chain:
            elems.append(str(last.value))
            last = last.next
        result = f"{' > '.join(elems)} > " if elems else "None"
        return result


def main():
    with open(file="input.txt", mode="r", encoding="utf-8") as f:
        _ = int(f.readline().strip())
        data = [value for value in map(int, f.readline().strip().split())]
    chain = Chain(data)
    round = 1
    while True:
        r = chain.round(round)
        round += 1
        if not r:
            break
    print(*chain.result)


if __name__ == "__main__":
    main()
