# D. Кирпичи

from itertools import product

def solve(a, s, l, n, i, j):
    pass


def main():
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    if sum(a)*2 < n:
        print(-1)
        return
    a.sort()
    for var in product(range(3), repeat=m):
        l = 0
        answer = []
        for i in range(len(var) - 1, -1, -1):
            if var[i] == 1:
                answer.append(a[i])
            elif var[i] == 2:
                answer.append(a[i])
                answer.append(a[i])
            l += a[i]*var[i]
            if l > n:
                break
        if l == n:
            print(len(answer))
            print(*answer)
            break
    else:
        print(0)


if __name__ == '__main__':
    main()
