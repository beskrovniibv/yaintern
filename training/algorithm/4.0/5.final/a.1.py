# A. Объединение последовательностей

def main():
    x = int(input())
    if x == 1:
        print(1)
        return
    # v = set()
    j = 1
    i1, i2 = 1, 1
    v1, v2 = 1, 1
    while j <= x:
        skip = False
        v1 = i1**2
        v2 = i2**3
        if v1 <= v2:
            i1 += 1
            if v1 == v2:
                i2 += 1
                # skip = True
            # if v1 in v:
            #     skip = True
            # else:
            #     v.add(v1)
        else:
            i2 += 1
            # if v2 in v:
            #     skip = True
            # else:
            #     v.add(v2)
        if not skip:
            j += 1
    print(v1 if v1 < v2 else v2)


if __name__ == '__main__':
    main()
