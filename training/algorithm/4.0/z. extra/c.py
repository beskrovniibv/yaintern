n = [1, 2, 3]
answer = [0] * len(n)
i1, i2 = 0, len(n) - 1
for i in range(len(n)):
    if n[i1]**2 > n[i2]**2:
        answer[len(n) - i - 1] = n[i1]**2
        i1 += 1
    else:
        answer[len(n) - i - 1] = n[i2]**2
        i2 -= 1
print(*answer)
