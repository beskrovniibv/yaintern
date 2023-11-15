#! usr/bin/python

# A. Дейкстра

class Solution:
    def solve(self, array: list[list[int]], start: int, finish: int) -> int:
        n = len(array[0]) + 1
        visited = [False]*n
        cnt = n - 1
        dist = [None]*n
        dist[start] = 0
        mn_idx = start
        while cnt > 0 and mn_idx:
            mn_val = None
            mn_idx = None
            for i in range(n):
                if (mn_val is None and dist[i] is not None) or (dist[i] < mn_val and not visited[i]):
                    mn_val = dist[i]
                    mn_idx = i
            if mn_idx is None:
                return -1
            for i, d in enumerate(array[mn_idx]):
                if not visited[i + 1]:
                    dist[i + 1] = d if dist[i + 1] is None else min(dist[i + 1], d)
        return dist[finish]


if __name__ == '__main__':
    n, s, f = map(int, input().split())
    array = [[0]*n]*n
    for i in range(n):
        row = list(map(int, input().split()))
        array[i] = row
    solution = Solution()
    answer = solution.solve(array, s, f)
    print(answer)
