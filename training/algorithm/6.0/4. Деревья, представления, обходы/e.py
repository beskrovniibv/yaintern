#! /usr/bin/python

# https://contest.yandex.ru/contest/66795/problems/E/

# E. Размер поддеревьев

tree = {}
weights = []


def dfs(node, parent):
    count = 1
    for child in tree[node]:
        if child != parent:
            count += dfs(child, node)
    weights[node - 1] = count
    return count


n = int(input())
weights = [0] * n
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    tree[v1] = tree.get(v1, [])
    tree[v1].append(v2)
    tree[v2] = tree.get(v2, [])
    tree[v2].append(v1)

dfs(1, 0)
print(*weights)
