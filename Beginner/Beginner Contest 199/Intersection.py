N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

lower = A[0]
upper = B[0]

for i in range(1, N):
    if lower <= A[i]:
        lower = A[i]
    if upper > B[i]:
        upper = B[i]

ans = 0
if lower <= upper:
    for i in range(lower, upper+1):
        ans += 1

print(ans)
