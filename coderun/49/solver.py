#! /usr/bin/python

from string import ascii_letters


def main():
    password = input().lower()
    print(len(password))
    while True:
        s = input()
        result = 0
        for i, c in enumerate(s):
            result += abs(ord(c) - ord(password[i]))
        print(result)
        if not result:
            return



if __name__ == "__main__":
    main()
