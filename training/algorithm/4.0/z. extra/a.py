#! usr/bin/python

""" За O(n) найти в массиве длины n подмассив длины k с наибольшей суммой элементов
"""


class Solution:
    def solve(self, n: int, k: int, array: list[int]) -> tuple[int, list[int]]:
        answer_array, frame = [], []
        frame_sum = 0
        max = None
        for i in range(n):
            if i < k:
                frame_sum += array[i]
                frame.append(array[i])
            else:
                frame_sum = frame_sum + array[i] - frame[0]
                frame = frame[1:]
                frame.append(array[i])
                if max is None or frame_sum > max:
                    max = frame_sum
                    answer_array = frame.copy()
        return max, answer_array


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    array = list(map(int, input().split()))
    solution = Solution()
    answer_int, answer_array = solution.solve(n, k, array)
    print(answer_int)
    print(*answer_array)
