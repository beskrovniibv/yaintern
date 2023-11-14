#! usr/bin/python

# E. Поразрядная сортировка

class Solution:
    def solve(self, array: list[str]) -> None:
        l = len(array[0]) - 1
        print('Initial array:')
        print(*array, sep=', ')
        bucket = {}
        for el in array:
            b = bucket.get(el[l], [])
            b.append(el)
            bucket[el[l]] = b
        for phase in range(len(array[0])):
            print('*' * 10)
            print(f'Phase {phase + 1}')
            for i in range(10):
                print(f'Bucket {i}: ', end='')
                print('empty') if bucket.get(str(i), '') == '' else print(*bucket[str(i)], sep=', ')
            l -=1
            if l < 0:
                break
            new_bucket = {}
            for i in range(10):
                b = bucket.get(str(i), [])
                if b:
                    for j in b:
                        nb = new_bucket.get(j[l], [])
                        nb.append(j)
                        new_bucket[j[l]] = nb
            bucket = new_bucket
        print('*' * 10)
        print('Sorted array:')
        ans = ''
        for i in range(10):
            b = bucket.get(str(i), [])
            if b:
                for e in b:
                    ans += f'{e}, '
            # print(*b, sep=', ', end=', ') if b else print(end='')
        while not ans[-1] in '0123456789':
            ans = ans[:-1]
        print(ans)

if __name__ == '__main__':
    n = int(input())
    array = [input() for _ in range(n)]
    solution = Solution()
    solution.solve(array)
