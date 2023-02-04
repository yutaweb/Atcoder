N, P, Q = map(int, input().split())
A = list(map(int, input().split()))


ans = 0
for i in range(N):
    p = A[i]
    for ii in range(i+1, N):
        pp = p * A[ii] % P
        for iii in range(ii+1, N):
            ppp = pp * A[iii] % P
            for iiii in range(iii+1, N):
                pppp = ppp * A[iiii] % P
                for iiiii in range(iiii+1, N):
                    if pppp * A[iiiii] % P == Q:
                        ans += 1

print(ans)
