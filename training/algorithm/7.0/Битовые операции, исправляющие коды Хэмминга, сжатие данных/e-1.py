#! /usr/bin/env python

def main():
    x, y = map(int, input().split())
    r1 = x ^ y
    c, x = map(int, input().split())
    r2 = c ^ x
    print(r1)
    print(r2)


if __name__ == "__main__":
    main()
