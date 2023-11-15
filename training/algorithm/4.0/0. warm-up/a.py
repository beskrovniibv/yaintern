#! usr/bin/python

# A. Не минимум на отрезке

class Solution():
    def solve(self, values, left, rigth):
        result = None
        minimum = values[left]
        for i in range(left, rigth + 1):
            if values[i] != minimum:
                result = max(values[i], minimum)
                break
        return result


if __name__ == '__main__':
    n, m = map(int, input().split())
    values = list(map(int, input().split()))
    solution = Solution()
    for _ in range(m):
        l, r = map(int, input().split())
        answear = solution.solve(values, l, r)
        print(answear) if answear is not None else print("NOT FOUND")
