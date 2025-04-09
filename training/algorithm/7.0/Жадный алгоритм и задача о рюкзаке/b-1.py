#! /usr/bin/env python

def solve(seq):
    result = []
    n = len(seq)
    l = 0
    while l < n:
        mn, mx = seq[l], seq[l]
        r = l + 1
        while mn > r - l and r < n:
            mn = min(mn, seq[r])
            if mn > r - l:
                r += 1
        result.append(str(r - l))
        l = r
    return result

    return ["0"]

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = solve(a)
    print(len(s))
    print(" ".join(s))
