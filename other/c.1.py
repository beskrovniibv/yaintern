#! usr/bin/python

def solve(n: int, nums: list[int]) -> list[int]:
    result = []
    last = nums[0]
    result.append(last)
    skip = 0
    for i in range(1, n):
        if nums[i] == last:
            skip += 1
        else:
            last = nums[i]
            result.append(last)
    result += ['_']*skip
    return result


if __name__ == '__main__':
    n = int(input())
    nums = [int(n) for n in input().split()]
    print(*solve(n, nums))
