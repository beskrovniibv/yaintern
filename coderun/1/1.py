#! usr/bin/python

# 1. Гвоздики

class Solution:
    def solve(self, n: int, nums: list[int]) -> int:
        nums = sorted(nums)
        dp = [0] * n
        dp[0] = nums[1] - nums[0]
        if n > 2:
            dp[1] = dp[0] + nums[2] - nums[1]
            for i in range(3, n):
                dp[i - 1] = min(dp[i - 3], dp[i - 2]) + nums[i] - nums[i - 1]
        return dp[n - 2]


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))

    # n = 6
    # nums = [3, 13, 12, 4, 14, 6]

    solution = Solution()
    answer = solution.solve(n, nums)
    print(answer)
