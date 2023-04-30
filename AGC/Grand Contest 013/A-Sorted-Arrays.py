N = int(input())
A = list(map(int, input().split()))

# 極大・極小を見つける
ans = 0
i = 0
while i < N:
    j = i
    while j + 1 < N and A[j] == A[j+1]:
        j += 1

    if j + 1 < N and A[j] < A[j+1]:
        # 単調増加
        while j + 1 < N and A[j] <= A[j+1]:
            j += 1
    elif j + 1 < N and A[j] > A[j+1]:
        # 単調減少
        while j + 1 < N and A[j] >= A[j+1]:
            j += 1

    ans += 1
    i = j + 1

print(ans)
