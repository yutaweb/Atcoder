# O(N)
N = int(input())
A = list(map(int, input().split()))

ans = 0
i = 0
while i < N:
    cnt = 0
    j = i
    while j < N and A[i] == A[j]:
        j += 1
        cnt += 1
    ans += cnt // 2
    i = j

print(ans)
