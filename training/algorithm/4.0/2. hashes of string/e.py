#! usr/bin/python

# E. Подпалиндромы


def toInt(c: str) -> int:
    return ord(c) - ord('0')


class Solution:
    def __init__(self, s: str):
        self.s = s
        self._x = 10
        self.n = len(s)
        self.prefix = [0] * (self.n + 1)
        self.suffix = [0] * (self.n + 1)
        self.x = [1] * (self.n + 1)
        self.p = 10**10 + 7

        for i, c in enumerate(self.s):
            if i == 0:
                self.prefix[i + 1] = (toInt(c)) % self.p
                self.suffix[i + 1] = (toInt(self.s[self.n - i - 1])) % self.p
                # self.x[i + 1] = 1
                continue
            self.prefix[i + 1] = (self.prefix[i]*self._x + toInt(c)) % self.p
            self.suffix[i + 1] = (self.suffix[i]*self._x + toInt(self.s[self.n - i - 1])) % self.p
            self.x[i] = (self.x[i - 1]*self._x) % self.p
        # for i in range(self.n, -1, -1):
        #     if i == 0:
        #         self.suffix[self.n - i - 1] = toInt(s[self.n - i - 1]) % self.p
        #         continue
        #     self.suffix[self.n - i - 1] = (self.suffix[self.n - i]*self._x + toInt(s[i])) % self.p

    # def compare(self, l: int, a: int, b: int) -> bool:
    #     h1 = (self.prefix[a + l] + self.prefix[b]*self.x[l]) % self.p
    #     h2 = (self.prefix[b + l] + self.prefix[a]*self.x[l]) % self.p
    #     return h1 == h2

    # def compare(self, length: int) -> int:
    #     if length*2 <= n:
    #         left = (self.prefix[2*length] + self.suffix[n - length] * self.x[length]) % self.p
    #         rigth = (self.suffix[self.n] + self.prefix[length]*self.x[length]) % self.p
    #     else:
    #         left = (self.prefix[2*length - 1] + self.suffix[n - length] * self.x[length]) % self.p
    #         rigth = (self.suffix[self.n] + self.prefix[length - 1]*self.x[length]) % self.p
    #     return left == rigth

    def check(self, left: int, length: int) -> bool:
        l, r = left, left + length
        prefix = self.prefix[r]
        prefix = prefix - self.prefix[l]*self.x[r - l]
        prefix = prefix % self.p

        l, r = self.n - (left + length), self.n - left
        suffix = self.suffix[r]
        suffix = suffix - self.suffix[l]*self.x[r - l]
        suffix = suffix % self.p
        # if length < self.n:
        #     suffix = self.suffix[self.n - left + length - 2]
        #     suffix = suffix - self.suffix[left]*self.x[length - 1]
        #     suffix = suffix % self.p
        # else:
        #     suffix = self.suffix[length - 1]
        #     suffix = suffix - self.suffix[left]*self.x[length - 1]
        #     suffix = suffix * self.x[self.n - length + 1]
        #     suffix = suffix + self.suffix[left]
        return prefix == suffix

    def solve(self) -> int:
        self.check(0, 10)
        self.check(0, 9)
        self.check(9, 1)
        self.check(3, 3)
        count = 0
        for i in range(self.n):
            pass
        return count


if __name__ == '__main__':
    # s = input()

    # 123
    s = '1234543216'

    solution = Solution(s)
    print(solution.solve())
