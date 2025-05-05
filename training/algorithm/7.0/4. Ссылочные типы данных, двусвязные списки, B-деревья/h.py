#! /usr/bin/env python

# H. Разрезание графа

import timeit

graph = {}
vertexes = []


def main():
    global vertexes
    global graph
    result = []
    with open(file="input.txt", mode="r", encoding="utf-8") as f:
        n, m, k = map(int, f.readline().strip().split())
        vertexes = [0] + [i for i in range(1, n + 1)]
        for i in range(1, n + 1):
            graph[i] = set([i])
        for _ in range(m):
            # u, v = map(int, f.readline().strip().split())
            f.readline()
            # graph[u].add(v)
            # graph[u].update(graph[v])
            # graph[v].add(u)
            # graph[v].update(graph[u])
        queries = []
        for _ in range(k):
            cmd, *args = f.readline().strip().split()
            u, v = map(int, args)
            queries.append((cmd, u, v))
            # if cmd.lower() == "ask":
            #     result.append(("NO", "YES")[len(graph[u].intersection(graph[v])) != 0])
            # elif cmd.lower() == "cut":
            #     vertexes[v] = v
            #     graph[v].discard(u)
            #     graph[u].discard(v)
            # else:
            #     assert "error: unknown command"
        count = n
        queries.reverse()
        for query in queries:
            cmd, u, v = query
            if cmd.lower() == "ask":
                result.append(("NO", "YES")[vertexes[u] == vertexes[v]])
            elif cmd.lower() == "cut":
                # lu, lv = len(graph[vertexes[u]]), len(graph[vertexes[v]])
                if vertexes[u] == vertexes[v]:
                    continue
                # if count == 1:
                #     continue
                gu, gv = graph[vertexes[u]], graph[vertexes[v]]
                lu, lv = len(gu), len(gv)
                if gu == gv:
                    pass
                elif lu and lu < lv:
                    for vertex in gu:
                        vertexes[vertex] = vertexes[v]
                    gv.update(gu)
                    graph[u] = {}
                    count -= 1
                elif lv and lv < lu:
                    for vertex in gv:
                        vertexes[vertex] = vertexes[u]
                    gu.update(gv)
                    graph[v] = {}
                    count -= 1
                elif lu:
                    for vertex in gu:
                        vertexes[vertex] = vertexes[v]
                    gv.update(gu)
                    graph[u] = {}
                    count -= 1
                else:
                    for vertex in gv:
                        vertexes[vertex] = vertexes[u]
                    gu.update(gv)
                    graph[v] = {}
                    count -= 1
            else:
                assert "ERROR: unknown command"
        with open(file="output.txt", mode="w", encoding="utf-8") as f:
            f.write(" ".join(map(str, reversed(result))))


if __name__ == "__main__":
    b = timeit.default_timer()
    main()
    e = timeit.default_timer()
    print(e - b)
