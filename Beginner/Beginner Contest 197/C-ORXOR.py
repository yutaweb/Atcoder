N = int(input())
A = list(map(int, input().split()))

min = 0
ans = 0
calc = 0

for i, base_val in enumerate(A):
    if i == 0:
        min = base_val^A[1]
    for j in range(i+1, N):
        calc = base_val^A[j]
        if min > calc:
            min = calc

ans = min
print(ans)