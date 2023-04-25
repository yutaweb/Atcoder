N = int(input())
S = input()

ans = 1
i = 0
while i < N-1:
    if S[i] != S[i+1]:
        ans += 1
    i += 1

print(ans)
