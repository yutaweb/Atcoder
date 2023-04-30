N = int(input())
A = list(map(int, input().split()))

# 極大・極小を見つける
ans = 0
i = 0
while i < N - 1:
    j = i
    print(j)
    if A[j] <= A[j+1]:
        # 単調増加
        while j < N - 1 and A[j] <= A[j+1]:
            j += 1
    else:
        # 単調減少
        while j < N - 1 and A[j] >= A[j+1]:
            j += 1
    print(i, j+1, A[i:j+1])
    ans += 1
    i = j + 1

print(ans)
