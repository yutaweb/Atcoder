N = int(input())

A = []
P = []
X = []
for i in range(N):
    a, p, x = map(int, input().split())
    A.append(a)
    P.append(p)
    X.append(x)

ans = int(1e10)

for i in range(N):
    if X[i] - A[i] - 1 >= 0:
        ans = min(ans, P[i])

if ans == int(1e10):
    print(-1)
else:
    print(ans)