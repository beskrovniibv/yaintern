#! usr/bin/python

# D. Кубики в зеркале


class Solution:
    def __init__(self, s: list[int], m: int, n: int):
        # self.s = ' ' + s
        self.s = [0] + s
        self.prefix = [0] * (len(s) + 1)
        self.suffix = [0] * (len(s) + 1)
        self.x = [0] * (len(s) + 1)
        self.p = 10**9 + 7
        # self._x = 10**6 + 7
        # self._x = m + 1
        self._x = 10
        self.n = n
        self.z = []
        self.a = set()
        for i, c in enumerate(self.s):
            if i == 0:
                self.x[0] = 1
                self.prefix[0] = 0
                continue
            self.prefix[i] = (self.prefix[i - 1]*self._x + c) % self.p
            self.x[i] = (self.x[i - 1]*self._x) % self.p
            self.a.add(c)
        j = -1
        for i in range(len(s), -1, -1):
            j += 1
            if i == len(s):
                self.suffix[j] = 0
                continue
            self.suffix[j] = (self.suffix[j - 1]*self._x + s[i]) % self.p
        if len(self.a) == 1:
            for i in range((n + 2 - 1)//2, n + 1):
                self.z.append(i)

    def compare(self, l: int, a: int, b: int) -> bool:
        h1 = (self.prefix[a + l] + self.prefix[b]*self.x[l]) % self.p
        h2 = (self.prefix[b + l] + self.prefix[a]*self.x[l]) % self.p
        return h1 == h2

    def compare_prefix_suffix(self, l: int, a: int) -> int:
        h1 = (self.prefix[a + l - 1] + self.suffix[a]*self.x[l]) % self.p
        h2 = (self.suffix[a + l - 1] + self.prefix[a]*self.x[l]) % self.p
        return h1 == h2

    def solve(self):
        if self.z:
            return self.z
        # if n % 2:
        #     return [n]
        result = [n]
        for i in range(2, n//2 + 2):
            if self.s[i - 1] != self.s[i]:
                continue
            # print(self.s[i - 1], self.s[i])
            l = n - i
            a = i
            if self.compare_prefix_suffix(l, a):
                result.append(n - i + 1)
            # h1 = (self.prefix[i + l - 1] + self.suffix[i]*self.x[l]) % self.p
            # h2 = (self.suffix[i + l - 1] + self.prefix[i]*self.x[l]) % self.p
            # if h1 == h2:
            #     result.append(n - i + 1)
            # if self.prefix[self.n - i + 1] == self.suffix[i - 1]:
            #     result.append(n - i + 1)
        return sorted(result)


if __name__ == '__main__':
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    solution = Solution(array, m, n)
    print(*solution.solve())
