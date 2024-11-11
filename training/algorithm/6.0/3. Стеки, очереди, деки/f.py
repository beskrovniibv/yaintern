#! /usr/bin/python

# https://contest.yandex.ru/contest/66794/problems/F/

# F. Минимальная ПСП

def solve(n, seq, sort):
    if n == len(seq):
        return seq
    st = []
    for ch in seq:
        if ch in "[(":
            st.append(ch)
        else:
            st.pop()
    ans = []
    if len(st) >= n//2:
        while st:
            ans.append("]") if st[-1] == "[" else ans.append(")")
            st.pop()
        return seq + "".join(ans)
    k = len(seq)
    while k < n:
        b = ""
        for c in sort:
            if st:
                if st[-1] == "[" and c == "]":
                    b = c
                    break
                if st[-1] == "(" and c == ")":
                    b = c
                    break
                if n - k - len(st) > 0 and c in "[(":
                    b = c
                    break
            else:
                if n - k - len(st) > 0 and c in "[(":
                    b = c
                    break
        ans.append(b)
        k += 1
        if b in "])":
            st.pop()
        else:
            st.append(b)
    return seq + "".join(ans)
    

n = int(input())
sort = input()
seq = input()

ans = solve(n, seq, sort)
print(ans)
