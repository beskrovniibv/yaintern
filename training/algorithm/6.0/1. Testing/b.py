def ans(a, b, c, d):
    m, n = 0, 0
    ans = []
    if a > 0 and c > 0:
        ans.append((b + d + 2, (b + 1, d + 1)))
    if b > 0 and d > 0:
        ans.append((a + c + 2, (a + 1, c + 1)))
    if a == b:
        ans.append((2*a + 1, (2*a, 1)))
    if c == d:
        ans.append((2*c + 1, (1, 2*c)))
    i = max(a, b) + 1
    if i < a + b:
        ans.append((i + 1, (i, 1)))
    i = max(c, d) + 1
    if i < c + d:
        ans.append((i + 1, (1, i)))
    m, n = sorted(ans)[0][1]
    return m, n


# a, b, c, d = (6, 2, 7, 3)
# assert ans(a, b, c, d) == (3, 4), "test #1"
# a, b, c, d = (1, 1, 1, 1)
# assert ans(a, b, c, d) == (1, 2), "test #2"
# a, b, c, d = (9, 0, 5, 2)
# assert ans(a, b, c, d) == (1, 3)
# a, b, c, d = (10, 7, 0, 4)
# assert ans(a, b, c, d) == (11, 1)
# a, b, c, d = (790, 493, 507, 302)
# assert ans(a, b, c, d) == (1, 508)


# a, b, c, d = (790, 493, 507, 302)

a, b, c, d = (int(input()) for _ in range(4))
a1, a2 = ans(a, b, c, d)
print(a1, a2)
