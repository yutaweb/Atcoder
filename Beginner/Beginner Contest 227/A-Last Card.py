N, K, A = map(int, input().split())
if N == 1:
    ans = N
else:
    if A == 1:
        ans = K % N
    else:
        cal = (K + (A - 1)) % N
        if cal == 0:
            ans = N
        else:
            ans = cal

print(ans)
