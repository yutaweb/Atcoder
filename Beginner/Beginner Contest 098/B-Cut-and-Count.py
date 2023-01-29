N = int(input())
S = input()

if len(set(S)) == 1:
    exit(print(1))

ans = 0
for i in range(N):
    common = 0
    A = set(S[:i+1])
    B = set(S[i+1:])
    if len(A) > len(B):
        for a in A:
            if a in B:
                common += 1
    else:
        for b in B:
            if b in A:
                common += 1
    ans = max(common, ans)

print(ans)
