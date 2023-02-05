N = int(input())

A = list(map(int, input().split()))

ans = 0
for l in range(N):
    num = A[l]
    for r in range(l, N):
        num = min(num, A[r])
        ans = max(ans, num*(r-l+1))
else:
    print(ans)
