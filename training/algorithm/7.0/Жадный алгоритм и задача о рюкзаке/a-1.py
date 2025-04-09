#! /usr/bin/env python

n, m = list(map(int, input().split()))
x = sorted([(x, i) for i, x in enumerate(map(int, input().split()))], reverse=True)
y = sorted([(y, i) for i, y in enumerate(map(int, input().split()))], reverse=True)

result = 0
answer = ["0"]*len(x)
l, r = 0, 0
for l in range(len(x)):
    if y[r][0] >= x[l][0] + 1:
        result += 1
        answer[x[l][1]] = str(y[r][1] + 1)
        r += 1

print(result)
print(" ".join(answer))