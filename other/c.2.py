#! usr/bin/python

def del_dublicates(data, a):
    uniq = ''
    set_2 = set(data)
    for j in sorted(list(set_2)):
        uniq += (str(j) + ' ')
    count = a - len(set_2)
    for i in range(count):
        uniq += '_ '
    return uniq.rstrip()


if __name__ == '__main__':
    a = int(input())
    data = list(map(int, input().split()))
    print(del_dublicates(data, a))
