#! usr/bin/python

# B. Быстрая сортировка

import sys
from random import randint, shuffle


class Solution:
    def partition(self, array: list[int], l: int, r: int, x: int) -> int:
        lt, eq, gt = l, l, l
        while gt <= r:
            y = array[gt]
            if array[gt] < x:
                array[gt] = array[eq]
                array[eq] = array[lt]
                array[lt] = y
                lt += 1
                eq += 1
                gt += 1
            elif array[gt] == x:
                array[gt] = array[eq]
                array[eq] = y
                gt += 1
                eq += 1
            elif array[gt] > x:
                gt += 1
        return lt, eq

    def quicksort(self, array: list[int], l: int, r: int) -> list[int]:
        if r - l < 1:
            return array
        x = array[randint(l, r)]
        # x = 2
        p1, p2 = self.partition(array, l, r, x)
        self.quicksort(array, l, p1 - 1)
        self.quicksort(array, p2, r)
        return array

    def solve(self, array: list[int]) -> list[int]:
        return self.quicksort(array, 0, len(array) - 1)


if __name__ == '__main__':
    sys.setrecursionlimit(1000)
    n = int(input())
    if n > 0:
        array = list(map(int, input().split()))
        # array = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        # shuffle(array)
        solution = Solution()
        sorted = solution.solve(array)
        print(*sorted)
