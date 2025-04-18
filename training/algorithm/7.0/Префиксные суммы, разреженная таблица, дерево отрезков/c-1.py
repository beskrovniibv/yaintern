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
        self.seq = [(-1, -1)]*(2*(self.n) - 1)
        for j in range(n):
            self.seq[self.n + j - 1] = (seq[j], j + 1)
        for j in range(self.n - 2, -1, -1):
            l, r = self.seq[2*j + 1], self.seq[2*j + 2]
            if l[0] == r[0]:
                self.seq[j] = (l[0], l[1])
            elif l[0] > r[0]:
                self.seq[j] = (l[0], l[1])
            else:
                self.seq[j] = (r[0], r[1])

    def find(self, l, r):
        def find(v, a, b, l, r):
            if a > r or b < l:
                return -1, 0
            if a >= l and b <= r:
                return self.seq[v]
            m = (a + b) // 2
            lv, lc = find(v*2 + 1, a, m, l, r)
            rv, rc = find(v*2 + 2, m + 1, b, l, r)
            if lv == rv:
                return lv, lc
            elif lv > rv:
                return lv, lc
            else:
                return rv, rc
        return find(0, 0, self.n - 1, l, r)


def main():
    n = int(input())
    seq = list(map(int, input().split()))
    tree = SegTree(n=n, seq=seq)
    k = int(input())
    result = [None]*k
    for i in range(k):
        l, r = map(int, input().split())
        result[i] = tree.find(l=l - 1, r=r - 1)
    for r in result:
        print(*r)


if __name__ == "__main__":
    main()
