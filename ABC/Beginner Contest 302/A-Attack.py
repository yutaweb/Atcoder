A, B = map(int, input().split())
tmp = divmod(A, B)

ans = tmp[0]
if tmp[1] != 0:
    ans += 1

print(ans)
