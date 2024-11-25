#! /usr/bin/python

# https://contest.yandex.ru/contest/66795/problems/F/

# F. Бюрократия
import sys


sys.setrecursionlimit(3_000_000)

tree = {}
ans = []


def dfs(node, salary=0):
    if node not in tree:
        ans[node] = 1
        return 1, 1
    size = 1
    salary = 0
    for e in tree[node]:
        sz, salary = dfs(e)
        size += sz
        ans[node] += salary
        # salary += 1
    ans[node] += size
    return size, ans[node]


with open("input.txt") as f:
    n = int(f.readline().strip())
    data = list(map(int, f.readline().strip().split()))
data = [0, 0] + data
ans = [0] + [0]*n

for i, el in enumerate(data):
    if i < 2:
        continue
    tree[el] = tree.get(el, [])
    tree[el].append(i)
data = []
dfs(1)

print(*ans[1:])
