#! /usr/bin/python

# https://contest.yandex.ru/contest/66793/problems/F/

# F. Сумма тройных произведений

MOD = 1_000_000_007


def solve(n, data):
    result = 0
    pref = [0] * (n + 1)
    prefm = [0] * (n + 1)
    pref2 = [0] * (n + 2)
    for i, v in enumerate(data):
        pref[i + 1] = (pref[i] + v) % MOD
    for i, v in enumerate(data):
        prefm[i + 1] = v*(pref[n] - pref[i + 1])
    for i, v in enumerate(prefm):
        pref2[i + 1] = (pref2[i] + v) % MOD
    for i, v in enumerate(data):
        result = (result + v*(pref2[n] - pref2[i + 2])) % MOD
    return result


def debug():
    assert solve(3, [1, 2, 3]) == 6
    assert solve(4, [0, 5, 6, 7]) == 210
    assert solve(5, [10, 6, 10, 3, 7]) == 3346
    assert solve(3, [143461, 574468, 902994]) == 630987644
    assert solve(10, [554786, 761671, 251576, 783746, 228900, 869195, 415433, 717481, 821644, 17214]) == 200122898
    print("Well done")


# debug()
n = int(input())
data = list(map(int, input().split()))
result = solve(n, data)
print(result)
