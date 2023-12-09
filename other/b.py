#! usr/bin/python

def solve(n: int, nums: list[int]) -> int:
    result = 1
    start = 0
    mn = nums[start]
    mx = nums[start]
    for i in range(1, n):
        len = i - start
        if len == mx - mn + 1 and i == mx + 1:
            result += 1
            start = i
            mn = nums[start]
            mx = nums[start]
        else:
            mn = min(mn, nums[i])
            mx = max(mx, nums[i])
    return result


if __name__ == '__main__':
    n = int(input())
    nums = [int(i) for i in input().split()]
    print(solve(n, nums))
