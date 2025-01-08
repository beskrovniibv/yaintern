#! /usr/bin/python python python3

import sys


def main():
    n = int(input())
    str1 = "a"*(n - 1) + "a"
    print(str1)
    sys.stdout.flush()
    diff = int(input())
    if diff == 0:
        return
    l = n - 1
    guess = ""
    while True:
        str1 = guess + "z"*(len(guess) != n) + "a"*l
        print(str1)
        sys.stdout.flush()
        s2 = int(input())
        if not s2:
            break
        y = (25 - abs(s2 - diff))//2
        if diff > s2:
            c = 25 - y
        else:
            c = y
        l -= 1
        if l == -1:
            guess += chr(ord("a") + diff)
        else:
            guess += chr(ord("a") + c)
        diff -= c




if __name__ == '__main__':
    main()