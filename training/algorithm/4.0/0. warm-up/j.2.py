#! usr/bin/python

# J. Групповой проект

class Solution:
    def solve(self, n, a, b):
        if b > 2*a:
            return n >= a
        if a == b:
            return n % a == 0
        if n < a:
            return False        
        if n > a*(b - a + 1):
            return True
        dp = [0] * (n + 1)
        dp[a:b] = [1] * (b - a + 1)
        for i in range(b + 1, n + 1):
            if i % a == 0:
                dp[i] = 1
            l = i - b
            r = i - a
            if 1 in dp[l:r + 1]:
                dp[i] = 1
            else:
                dp[i] = 0
        return dp[n] != 0

if __name__ == '__main__':
    n = int(input())
    solution = Solution()
    for _ in range(n):
        n, a, b = map(int, input().split())
        print(("NO", "YES")[solution.solve(n, a, b)])
