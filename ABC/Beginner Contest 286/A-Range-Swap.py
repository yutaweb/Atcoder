N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))

B = A.copy()
B[P-1:Q] = A[R-1:S]
B[R-1:S] = A[P-1:Q]

print(*B)
