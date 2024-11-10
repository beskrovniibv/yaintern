#! /usr/bin/python

# https://contest.yandex.ru/contest/66793/problems/G/

# G. Цензурное произведение

def solve(n, c, s):
    p = [0] * (n + 1)
    for i, ch in enumerate(s):
        p[i + 1] = p[i] + (1 if ch == 'a' else 0)
    r = 0
    u = 0
    result = 0
    for l in range(n):
        u = p[r] - p[l] if p[r] - p[l] > 1 else 0
        while r  + 1 < n and u < c:
            r += 1
            if s[r] == "b":
                u += p[r] - p[l]
        result = max(result, r - l)
    return result


def debug():
    assert solve(3, 1, "aab") == 2
    assert solve(6, 2, "aabcbb") == 4
    print("Well done")


# debug()
n, c = map(int, input().split())
s = input()
result = solve(n, c, s)
print(result)
