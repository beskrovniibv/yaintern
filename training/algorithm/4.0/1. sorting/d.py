#! usr/bin/python

# D. Сортировка слиянием

class Solution:
    def merge(self, array1: list[int], array2: list[int]) -> list[int]:
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

    def sort(self, array: list[int]) -> list[int]:
        if len(array) <= 1:
            return array
        l = self.sort(array[0:len(array) // 2].copy())
        r = self.sort(array[len(array)//2: len(array)].copy())
        return self.merge(l, r)
        return 

    def solve(self, array: list[int]) -> list[int]:
        array = self.sort(array)
        return array


if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    solution = Solution()
    array = solution.solve(array)
    print(*array)
