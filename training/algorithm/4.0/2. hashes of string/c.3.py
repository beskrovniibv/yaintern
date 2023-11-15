def sym_to_num(sym):
    return ord(sym) - ord('a') + 1

def get_pows(cnt_pows, x, p):
    pows = [None] * cnt_pows
    pows[0] = 1
    for i in range(1, cnt_pows):
        pows[i] = (pows[i - 1] * x) % p
    
    return pows

def get_prefixs(string, x, p, sym_to_num):
    prefixs = [None] * (len(string) + 1)
    prefixs[0] = 0
    for i in range(1, len(string) + 1):
        prefixs[i] = (prefixs[i - 1] * x + sym_to_num(string[i - 1])) % p
    
    return prefixs

def is_equal(from1, from2, length, p, pows, prefixs):
    left_part = (prefixs[from1 + length] + prefixs[from2] * pows[length]) % p
    right_part = (prefixs[from2 + length] + prefixs[from1] * pows[length]) % p
    
    return left_part == right_part

def right_bin_search(r, from2, args):
    l = 0
    while r - l > 1:
        m = (l + r) // 2
        if is_equal(0, from2, m, *args):
            l = m
        else:
            r = m - 1
    
    return l


p = 10**6 + 3
x = 29

string = input()

pows = get_pows(len(string) + 1, x, p)
prefixs = get_prefixs(string, x, p, sym_to_num)
args = (p, pows, prefixs)

z = [0] * len(string)
for i in range(1, len(string)):
    from2 = i
    max_len = len(string) - from2 + 1
    if is_equal(0, from2, 1, *args):
        z[i] = right_bin_search(max_len, from2, args)

print(*z)