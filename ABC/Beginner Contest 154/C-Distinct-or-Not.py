N = int(input())
A = map(int, input().split())
check = set()

for a in A:
    check.add(a)

if len(check) == N:
    ans = "YES"
else:
    ans = "NO"

print(ans)
