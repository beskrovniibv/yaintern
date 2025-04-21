#! /usr/bin/env python

# https://contest.yandex.ru/contest/74966/problems/A/

class SegTree:
    _2 = {
        0: 1,
        1: 2,
        2: 4,
        3: 8,
        4: 16,
        5: 32,
        6: 64,
        7: 128,
        8: 256,
        9: 512,
        10: 1024,
        11: 2048,
        12: 4096,
        13: 8192,
        14: 16384,
        15: 32768,
        16: 65536,
        17: 131072,
    }

    def __init__(self, n, seq):
        j = 1
        while self._2[j] < n:
            j += 1
        self.n = self._2[j]
        self.seq = [-1]*(2*(self.n) - 1)
        for j in range(n):
            self.seq[self.n + j - 1] = seq[j]
        for j in range(self.n - 2, -1, -1):
            l, r = self.seq[2*j + 1], self.seq[2*j + 2]
            self.seq[j] = max(r, l)

    def find(self, l, r):
        def find(v, a, b, l, r):
            if a > r or b < l:
                return -1
            if a >= l and b <= r:
                return self.seq[v]
            m = (a + b) // 2
            lv = find(v*2 + 1, a, m, l, r)
            rv = find(v*2 + 2, m + 1, b, l, r)
            if lv == rv:
                return lv
            elif lv > rv:
                return lv
            else:
                return rv
        return find(0, 0, self.n - 1, l, r)

    def update(self, i, value):
        k = i + self.n - 2
        self.seq[k] = value
        while k > 0:
            k = (k - 1)//2
            self.seq[k] = max(
                self.seq[2*k + 1],
                self.seq[2*k + 2]
            )


def main():
    n = int(input())
    seq = list(map(int, input().split()))
    tree = SegTree(n=n, seq=seq)
    k = int(input())
    result = []
    for i in range(k):
        o, *op = input().split()
        op1, op2 = map(int, op)
        if o == 's':
            result.append(tree.find(l=op1 - 1, r=op2 - 1))
        else:
            tree.update(i=op1, value=op2)
    print(*result)


if __name__ == "__main__":
    main()
