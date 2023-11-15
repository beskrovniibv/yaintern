def f(x, y):
    if x > y:
        k = y
    else:
        k = x
    for i in range(1, k + 1):
        if x % i == 0 and y % i == 0:
            nod = i
    return nod


a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a <= 100 and b <= 100 and c <= 100 and d <= 100 and b != 0 and d != 0:
    m = int(a*d/(f(b, d)) + c*b/(f(b, d)))
    n = int(b*d/(f(b, d)))
    nod = f(m, n)
    m = int(m / nod)
    n = int(n / nod)
    print(m, n)
