#! /usr/bin/python

# https://contest.yandex.ru/contest/66795/problems/B/

# B. Родословная: число потомков

import sys
sys.setrecursionlimit(1_000_000)

tree = {}
tree1 = {}
childs = {}

def get_child_count(key):
    if not tree1.get(key):
        childs[key] = 0
        return 0
    child = 0
    for c in tree1[key]:
        child += get_child_count(c)
    child += len(tree1[key])
    childs[key] = child
    return child


n = int(input())

for _ in range(n - 1):
    child, parent = input().split()
    tree[child] = parent
    node = tree1.get(parent)
    if node:
        node.append(child)
    else:
        tree1[parent] = [child]

root = (set(tree.values()) - set(tree.keys())).pop()

get_child_count(root)

for key in sorted(childs.keys()):
    print(key, childs[key])
