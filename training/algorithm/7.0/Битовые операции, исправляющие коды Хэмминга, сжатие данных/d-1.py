#! /usr/bin/env python

def bcount(value):
    result, bits = 0, 0
    while value:
        result += value & 1
        value >>= 1
        bits += 1
    return result, bits


def main():
    n = int(input())
    _, w = bcount(n)
    mask = 0
    for i in range(w):
        mask = mask << 1 | 1
    mx = n
    for i in range(w):
        h = n >> (w - 1)
        n = ((n << 1) & mask) | h
        mx = max(mx, n)
    return mx


if __name__ == "__main__":
    result = main()
    print(result)
