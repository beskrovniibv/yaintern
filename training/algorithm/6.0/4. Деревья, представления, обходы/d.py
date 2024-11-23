#! /usr/bin/python

# https://contest.yandex.ru/contest/66795/problems/D/

# D. Бинарное дерево (вставка, поиск, обход)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.rigth = None

    def __repr__(self):
        return f"<{self.value}>"


class Tree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return True
        node = self.root
        while True:
            if value > node.value:
                if node.rigth:
                    node = node.rigth
                else:
                    node.rigth = Node(value)
                    break
            elif value < node.value:
                if node.left:
                    node = node.left
                else:
                    node.left = Node(value)
                    break
            else:
                return False
        return True

    def search(self, value):
        def searchvalue(root, value):
            if value > root.value:
                if root.rigth:
                    return searchvalue(root.rigth, value)
                return False
            elif value < root.value:
                if root.left:
                    return searchvalue(root.left, value)
                return False
            else:
                return True
        return searchvalue(self.root, value) if self.root else False

    def printtree(self):
        def printnode(root, path):
            if root.left:
                tpath = path.copy()
                tpath.append(".")
                printnode(root.left, tpath)
            print("".join(path), root.value, sep="")
            if root.rigth:
                tpath = path.copy()
                tpath.append(".")
                printnode(root.rigth, tpath)
        printnode(self.root, [])


tree = Tree()
with open("input.txt") as f:
    while f:
        line = f.readline().strip()
        if not line:
            break
        line = line + " 0"
        cmd, *arg = line.split()
        if cmd.lower() == "add":
            print(("ALREADY", "DONE")[tree.add(int(arg[0]))])
        elif cmd.lower() == "search":
            print(("NO", "YES")[tree.search(int(arg[0]))])
        elif cmd.lower() == "printtree":
            tree.printtree()
