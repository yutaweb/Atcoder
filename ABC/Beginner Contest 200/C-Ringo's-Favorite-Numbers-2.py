# 計算量：O(N) ※ 2*2*N
from collections import Counter


N = int(input())
A = list(map(int, input().split()))
C = Counter()

for i in range(N):
    A[i] = A[i] % 200

ans = 0
for j in range(N):
    ans += C[A[j]]
    C[A[j]] += 1

print(ans)
