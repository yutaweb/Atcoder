N = int(input())
H = list(map(int, input().split()))

ans = 0
i = 0
while i < N-1:
    j = i
    while j < N-1 and H[j] >= H[j+1]:
        j += 1

    ans = max(ans, j-i)
    i = j+1

print(ans)
