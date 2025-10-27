#! /usr/bin/env

# F. Железнодорожный переезд

# https://contest.yandex.ru/contest/80942/problems/F/

n, m, x = map(int, input().split())
events = [0]*n
for i in range(n):
    a, b, v = map(int, input().split())
    if a > b:
        a, b = b, a
        v = -v
    length = b - a
    t1 = (x - a) / v
    t2 = (x - b) / v
    if t1 > t2:
        t1, t2 = t2, t1
    events[i] = (t1, t2)  # приехал
    # events[i*2 + 1] = (t2, 1)  # уехал
_events = []
current = None
for e in sorted(events):
    begin, end = e
    if current is None:
        current = [begin, end]
    else:
        if begin > current[1]:
            _events.append(current)
            current = [begin, end]
        elif end > current[1]:
            current[1] = end
_events.append(current)
# print(_events)
queries = list(map(int, input().split()))
_queries = sorted([(q, i) for i, q in enumerate(queries)])
# print(_queries)
result = [0]*m
i, j = 0, 0
while i < m and j < len(_events):
    t1, c1 = _queries[i]
    b1, e1 = _events[j]
    if t1 < b1:
        result[c1] = f"{t1:f}"
        i += 1
        continue
    if t1 >= b1 and t1 <= e1:
        result[c1] = f"{e1:f}"
        i += 1
        continue
    if t1 > e1:
        j += 1
for i in range(i, m):
    result[_queries[i][1]] = f"{_queries[i][0]:f}"
print("\n".join(result))
