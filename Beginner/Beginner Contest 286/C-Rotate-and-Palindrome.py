# 方針
# 1. Bのみ
# 2. AとB両方
# 提出時は、基本的にPyPyで提出するべき

N, A, B = map(int, input().split())
S = input()

ans = 10 ** 100
for i in range(N):
    b = 0
    if i != 0:
        S = S[1:] + S[0]

    for j in range(N // 2):
        if S[j] != S[N - 1 - j]:
            b += 1

    cost = A * i + B * b

    ans = min(ans, cost)

print(ans)
