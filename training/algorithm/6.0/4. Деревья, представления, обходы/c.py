#! /usr/bin/python

# https://contest.yandex.ru/contest/66795/problems/C/

# C. Родословная: LCA

nodes = {}

childs = set()
parents = set()
tree = {}
paths = {}
root = ''


def get_path(node, path):
    path.append(node)
    paths[node] = path
    if node not in tree:
        return
    for child in tree[node]:
        get_path(child, path.copy())


def lca(node1, node2):
    result = root
    for i in range(min(len(paths[node1]), len(paths[node2]))):
        if paths[node1][i] != paths[node2][i]:
            break
        result = paths[node1][i]
    return result


with open("input.txt") as f:
    data = f.readlines()
n = int(data[0])

for i in range(n - 1):
    child, parent = data[i + 1].split()
    childs.add(child)
    parents.add(parent)
    nodes[child] = None
    nodes[parent] = None
    tree[parent] = tree.get(parent, [])
    tree[parent].append(child)

root = (parents - childs).pop()

get_path(root, [])
i += 1
while i < len(data) - 1:
    node1, node2 = data[i + 1].split()
    print(lca(node1, node2))
    i += 1
