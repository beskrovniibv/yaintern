#! usr/bin/python

# C. Z-функция

class Solution:
    def __init__(self, s: str):
        self.s = s
        self.z = [0] * len(s)

    def solve(self):
        left, right = 0, 0
        for i in range(1, len(self.s)):
            self.z[i] = max(0, min(self.z[i - left], right - i))
            while i + self.z[i] < len(self.s) and self.s[self.z[i]] == self.s[i + self.z[i]]:
                self.z[i] += 1
            if i + self.z[i] > right:
                left, right = i, i + self.z[i]
        return self.z


if __name__ == '__main__':
    s = input()
    solution = Solution(s)
    print(*solution.solve())
