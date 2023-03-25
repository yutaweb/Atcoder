N, K = map(int, input().split())

num = [0]*N
for i in range(1, N + 1):
    num[i % K] += 1

res = 0
for a in range(K):
    c = (K - a) % K
    b = (K - a) % K
    if (b + c) % K != 0:
        continue
    res += num[a] * num[b] * num[c]

print(res)
