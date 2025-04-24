#! /usr/bin/env python

def main():
    n = int(input())
    result = 0
    while n:
        result += n & 1
        n >>= 1
    print(result)


if __name__ == "__main__":
    main()
