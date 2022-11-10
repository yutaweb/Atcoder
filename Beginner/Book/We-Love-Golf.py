K = int(input())
A, B = map(int, input().split())

for v in range(A, B + 1):
    if v % K == 0:
        ans = "OK"
        break

print(ans)

# print("OK" if exist else "NG")
