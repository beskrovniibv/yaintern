#! /usb/bin/python

# https://contest.yandex.ru/contest/66793/problems/E/

# E. Удаление медиан

def solve(n, data):
    result = [0] * n
    r = n // 2 + n % 2
    l = r - 1
    m = l
    i = 0
    while i < n:
        if (n - i) & 1 == 1:
            result[i] = data[m]
            if m == l:
                l -= 1
            else:
                r += 1
        else:
            if (r == n) or (data[l] < data[r]):
                result[i] = data[l]
                m = r
                l -= 1
            else:
                result[i] = data[r]
                m = l
                r += 1
        i += 1
    return result


def debug():
    n = 3
    data = [19, 3, 8]
    assert solve(n, sorted(data)) == [8, 3, 19]

    n = 4
    data = [1, 2, 4, 2]
    assert solve(n, sorted(data)) == [2, 2, 1, 4]

    n = 4
    data = [10, 0, 10, 10]
    assert solve(n, sorted(data)) == [10, 10, 0, 10]

    n = 4
    data = [4, 0, 2, 0]
    assert solve(n, sorted(data)) == [0, 2, 0, 4]


# debug()
n = int(input())
data = list(map(int, input().split()))
ans = solve(n, sorted(data))
print(*ans)
