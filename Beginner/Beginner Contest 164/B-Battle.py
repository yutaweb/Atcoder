A, B, C, D = map(int, input().split())

ans = "No"
while 0 < A:
    C = C - B
    if C <= 0:
        ans = "Yes"
    A = A - D

print(ans)
