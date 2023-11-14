#! usr/bin/python

# C. Слияние

class Solution:
    def solve(self, array1: list[int], array2: list[int]) -> list[int]:
        if len(array1) == 0:
            return array2
        if len(array2) == 0:
            return array1
        i, j = 0, 0
        array = []
        while True:
            if array1[i] <= array2[j]:
                array.append(array1[i])
                i += 1
            else:
                array.append(array2[j])
                j += 1
            if i >= len(array1):
                array += array2[j:]
                break
            if j >= len(array2):
                array += array1[i:]
                break
        return array
        pass


if __name__ == '__main__':
    n = int(input())
    array_1 = list(map(int, input().split()))
    m = int(input())
    array_2 = list(map(int, input().split()))
    solution = Solution()
    array = solution.solve(array_1, array_2)
    print(*array)
    pass
