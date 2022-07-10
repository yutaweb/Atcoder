N, M, X, T, D = map(int, input().split())

if M == 0:
    if X == N:
        ans = T-N*D
    else:
        ans = T-X*D
elif X <= M:
    ans = T
else:
    ans = T-(X-M)*D

print(ans)
