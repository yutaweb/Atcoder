N, K = map(int, input().split())
L = list(map(int, input().split()))

L.sort(reverse=True)

ans = sum(L[:K])

print(ans)
