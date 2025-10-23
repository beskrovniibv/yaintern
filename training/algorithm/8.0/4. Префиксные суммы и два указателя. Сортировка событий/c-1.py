#! /usr/bin/env

# C. Очередь из кандидатов

# https://contest.yandex.ru/contest/80942/problems/C/

n, k = map(int, input().split())
leave, left = 0, 0
arr = list(map(int, input().split()))
res = [0]*n
for i in range(n):
    if i == 0:
        prev = 0
    else:
        prev = res[i - 1]
    res[i] = prev + (1 if arr[i] >= k else 0)
m = int(input())
result = []
for _ in range(m):
    q, *arg = map(int, input().split())
    if q == 1:  # добавить в конец
        arr.append(arg[0])
        res.append(res[-1] + (1 if arg[0] >= k else 0))
    elif q == 2:  # убрать из начала
        leave += (1 if arr[left] >= k else 0)
        left += 1
    elif q == 3:  # ответить на запрос
        if arg[0] == 0:
            result.append(0)
            continue
        ans = res[arg[0] + left - 1] - leave
        if ans < 0:
            ans = 0
        result.append(ans)
    else:
        assert "error"
print(*result, sep="\n")
