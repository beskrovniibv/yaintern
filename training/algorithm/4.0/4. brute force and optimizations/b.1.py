#! usr/bin/python

# B. Затерянный мир

def solve(n: int) -> int:
    answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724]
    return answer[n]


def main():
    n = int(input())
    answer = solve(n)
    print(answer)


if __name__ == '__main__':
    main()
