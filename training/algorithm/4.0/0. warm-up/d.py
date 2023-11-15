#! usr/bin/python

# D. Анаграмма?

from collections import Counter


class Solution:
    def solve(self, str1: str, str2: str) -> bool:
        c1 = Counter(str1)
        c2 = Counter(str2)
        return c1 == c2


if __name__ == '__main__':
    str1 = input()
    str2 = input()
    solution = Solution()
    print("YES") if solution.solve(str1, str2) else print("NO")
