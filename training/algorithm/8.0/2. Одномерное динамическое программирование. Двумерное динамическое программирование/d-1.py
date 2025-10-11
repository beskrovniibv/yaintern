s = input()
n = int(input())
d = set()
for _ in range(n):
    d.add(input())
l = len(s)
dp = [False]*(l + 1)
nx = [-1]*(l + 1)
dp[l] = True
for i in range(l - 1, -1, -1):
    for j in range(i + 1, l + 1):
        w = s[i:j]
        if w in d and dp[j]:
            dp[i] = True
            nx[i] = j
            break

result = []
n = 0
while i != -1 and i < l:
    n = nx[i]
    if n == -1:
        break
    result.append(s[i:n])
    i = n

print(' '.join(result))