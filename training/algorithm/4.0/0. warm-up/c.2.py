#! usr/bin/python

# C. Путешествие по Москве

class Solution:
    def solve(self, x1, y1, x2, y2):
        r1 = (x1**2 + y1**2)**.5
        r2 = (x2**2 + y2**2)**.5
        print(r1, r2)
        pass


if __name__ == '__main__':
    xA, yA, xB, yB = map(int, input().split())
    solution = Solution()
    print(solution.solve(xA, yA, xB, yB))
