#! usr/bin/python

# A. Partition

class Solution:
    def solve(self, n: int, array: list[int], x: int) -> tuple[int, int]:
        l, r = 0, 0
        for el in array:
            if el < x:
                l += 1
        r = n - l
        return l, r


if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    x = int(input())
    solution = Solution()
    l, r = solution.solve(n, array, x)
    print(f'{l}\n{r}')
