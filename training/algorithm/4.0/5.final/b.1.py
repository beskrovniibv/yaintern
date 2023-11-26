# B. Зеркальная z-функция

#! usr/bin/python

# C. Z-функция

def toint(value: str) -> int:
    return ord(value) - ord('0')

class Solution:
    def __init__(self, s: str):
        self.s = s
        self.n = len(s)
        self.prefix = [0] * (self.n + 1)
        self.suffix = [0] * (self.n + 1)
        self.x = [1] * (self.n + 1)
        self.p = 10**9 + 7
        self._x = 10
        for i, c in enumerate(self.s):
            if i == 0:
                self.prefix[i + 1] = (toint(c)) % self.p
                self.suffix[i + 1] = (toint(self.s[self.n - i - 1])) % self.p
                continue
            self.prefix[i + 1] = (self.prefix[i]*self._x + toint(c)) % self.p
            self.suffix[i + 1] = (self.suffix[i]*self._x + toint(self.s[self.n - i - 1])) % self.p
            self.x[i] = (self.x[i - 1]*self._x) % self.p

    def find(self, l: int, a: int, b: int) -> bool:
        h1 = (self.prefix[a + l] + self.prefix[b]*self.x[l]) % self.p
        h2 = (self.prefix[b + l] + self.prefix[a]*self.x[l]) % self.p
        return h1 == h2

    def check(self, left: int, length: int) -> bool:
        l, r = 0, length
        prefix = self.prefix[r]
        prefix = prefix - self.prefix[l]*self.x[r - l]
        prefix = prefix % self.p

        l, r = self.n - (left + length), self.n - left
        suffix = self.suffix[r]
        suffix = suffix - self.suffix[l]*self.x[r - l]
        suffix = suffix % self.p

        return prefix == suffix

    def solve(self) -> list[int]:
        answer = [1]
        for i in range(1, len(self.s)):
            right = i + 1
            left = 1
            while right - left > 1:
                middle = (left + right)//2
                if self.check(middle, i):
                    left = middle
                else:
                    right = middle
            answer.append(right)
        return answer
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
    n = input()
    s = input()
    solution = Solution(s)
    print(*solution.solve())
