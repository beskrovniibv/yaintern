#! /usr/bin/python

# C. Путешествие по Москве

from math import atan2


class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cross_product(self, b):
        return self.x*b.y - self.y*b.x

    def dot_product(self, b):
        return self.x*b.x + self.y*b.y


class Solution:
    def solve(self, x1, y1, x2, y2):
        v1 = Vector(x1, y1)
        v2 = Vector(x2, y2)
        r1 = (x1**2 + y1**2)**0.5
        r2 = (x2**2 + y2**2)**0.5
        phi = abs(atan2(v1.cross_product(v2), v1.dot_product(v2)))
        l1 = r1 + r2
        l2 = abs(r1 - r2) + min(r1, r2)*phi
        return min(l1, l2)


if __name__ == '__main__':
    xA, yA, xB, yB = map(int, input().split())
    solution = Solution()
    print(solution.solve(xA, yA, xB, yB))
