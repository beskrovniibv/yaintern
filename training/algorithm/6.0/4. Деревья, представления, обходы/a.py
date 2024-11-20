#! /usr/bin/python

# https://contest.yandex.ru/contest/66795/problems/A/

# A. Родословная: подсчет уровней

tree = {}
heights = {}

def get_height(key):
    if key in heights:
        return heights[key]
    if key not in tree.keys():
        heights[key] = 1
        return 1
    height = get_height(tree[key]) + 1
    heights[key] = height
    return height


n = int(input())

for _ in range(n - 1):
    child, parent = input().split()
    tree[child] = parent

root = (set(tree.values()) - set(tree.keys())).pop()

heights[root] = 0

for node in tree.keys():
    get_height(node)

for key in sorted(heights.keys()):
    print(key, heights[key])
