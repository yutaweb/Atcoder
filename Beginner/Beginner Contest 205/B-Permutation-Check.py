N = int(input())
A = list(map(int, input().split()))

A.sort()

A_dummy = [a + 1 for a in range(N)]

if A == A_dummy:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)
