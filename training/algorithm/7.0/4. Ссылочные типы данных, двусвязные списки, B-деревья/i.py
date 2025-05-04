#! /usr/bin/env python

# I. Снеговики

class Node():
    def __init__(self, weight, value):
        self.value = value
        self.weight = weight + value
        self.prev = None

    def __repr__(self):
        return f"{self.value} ({self.weight})"


def main():
    result = 0
    with open(file="input.txt", mode="r", encoding="utf-8") as f:
        n = int(f.readline().strip())
        # snowman = [(None, None, 0)] + [0]*n  # head tail weight
        snowman = [Node(0, 0)] + [None]*n
        # parents = [0] + [0]*n
        for i in range(1, n + 1):
            p, h = map(int, f.readline().strip().split())
            if h != 0:
                # node = Node(h)
                parent = snowman[p]
                node = Node(parent.weight, h)
                node.prev = parent
                snowman[i] = node
            else:
                snowman[i] = snowman[p].prev
            # head = h
            # if h == 0:
            #     tail = snowman[p][1]
            #     if snowman[p][0] == 0:
            #         tail = snowman[snowman[p][1]][1]
            #     weight = snowman[tail][2]
            # else:
            #     tail = p
            #     weight = snowman[tail][2] + head
            # snowman[i] = (head, tail, weight)
            result += snowman[i].weight
    for s in snowman:
        print(s.weight)
    return result


if __name__ == "__main__":
    ans = main()
    print(ans)
