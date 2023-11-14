#! usr/bin/python

# C. Z-функция

class Solution:
    def __init__(self, s: str):
        self.s = ' ' + s
        self.hash = [0] * (len(s) + 1)
        self.x = [0] * (len(s) + 1)
        self.p = 10**9 + 7
        self._x = 257
        self.z = [0] * (len(self.s) - 1)
        for i, c in enumerate(self.s):
            if i == 0:
                self.x[0] = 1
                self.hash[0] = 0
                continue
            coef = ord(c)
            self.hash[i] = (self.hash[i - 1]*self._x + coef) % self.p
            self.x[i] = (self.x[i - 1]*self._x) % self.p

    def find(self, l: int, a: int, b: int) -> bool:
        h1 = (self.hash[a + l] + self.hash[b]*self.x[l]) % self.p
        h2 = (self.hash[b + l] + self.hash[a]*self.x[l]) % self.p
        return h1 == h2

    def solve(self) -> list[int]:
        for i, s in enumerate(self.s):
            if i < 2:
                continue
            if s != self.s[1]:
                continue
            else:
                right = len(self.s) - i + 1
                left = 1
                while right - left > 1:
                    middle = (left + right)//2
                    if self.find(middle, 0, i - 1):
                        left = middle
                    else:
                        right = middle
                self.z[i - 1] = left
        return self.z


if __name__ == '__main__':
    s = input()
    solution = Solution(s)
    print(*solution.solve())
