#! usr/bin/python

# A. Равенство подстрок

class Solution:
    def __init__(self, s: str):
        self.s = ' ' + s
        self.hash = [0] * (len(s) + 1)
        self.x = [0] * (len(s) + 1)
        self.p = 10**9 + 7
        self._x = 257
        for i, c in enumerate(self.s):
            if i == 0:
                self.x[0] = 1
                self.hash[0] = 0
                continue
            # coef = ord(c) - ord('a') + 1
            coef = ord(c)
            self.hash[i] = (self.hash[i - 1]*self._x + coef) % self.p
            self.x[i] = (self.x[i - 1]*self._x) % self.p

    def solve(self, l: int, a: int, b: int) -> bool:
        h1 = (self.hash[a + l] + self.hash[b]*self.x[l]) % self.p
        h2 = (self.hash[b + l] + self.hash[a]*self.x[l]) % self.p
        return h1 == h2


if __name__ == '__main__':
    s = input()
    q = int(input())
    solution = Solution(s)
    for _ in range(q):
        l, a, b = map(int, input().split())
        print(('no', 'yes')[solution.solve(l, a, b)])
