N = int(input())
S = list(map(int, input().split()))

# S.sort()

ans = [S[0]]
for i in range(N - 1):
    ans.append(S[i + 1] - S[i])

print(*ans)
