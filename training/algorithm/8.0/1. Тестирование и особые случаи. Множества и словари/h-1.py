n, m = map(int, input().split())
s = input()
f = []
d = {}
i = 1
for _ in range(m):
    t = input()
    f.append(t)
    d[t] = d.get(t, [0, []])
    d[t][1].append(i)
    i += 1
l = n//m
i = 0
result = []
for _ in range(m):
    t = s[i:i + l]
    result.append(d[t][1][d[t][0]])
    d[t][0] += 1
    i += l
print(*result)