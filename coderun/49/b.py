#! usr/bin/python

from random import choice
from string import ascii_lowercase
from itertools import combinations_with_replacement as combinations

ABC = ascii_lowercase
strings = list(combinations(ABC, 2))

counter = 0


def dist(password: str, string: str) -> int:
    global counter
    counter += 1
    assert len(password) == len(string), "Lengths are not equal"
    length = len(password)
    result = 0
    for index in range(length):
        ch1, ch2 = password[index], string[index]
        result += abs(ord(ch1) - ord(ch2))
    return result


def main():
    global counter
    password = choice(ABC) + choice(ABC)
    # password = 'y'
    l = 0
    r = len(strings)
    while r - l > 1:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3 - 1
        d1 = dist(password, strings[mid1])
        d2 = dist(password, strings[mid2])
        if d1 < d2:
            r = mid2
        else:
            l = mid1 + 1
    string = ''.join(strings[l])
    print(f'{password} was found on {counter} steps: {string}')


if __name__ == '__main__':
    main()
