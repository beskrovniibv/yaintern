#! /usr/bin/env python

def main():
    n = int(input())
    result = [0]*n
    for i in range(n):
        r = map(int, input().split())
        for j, v in enumerate(r):
            if i == 0 and j == 0:
                continue
            result[i] |= v
            result[j] |= v
    print(*result)


if __name__ == "__main__":
    main()
