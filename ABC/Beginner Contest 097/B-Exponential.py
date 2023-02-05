X = int(input())

ans = 0

for b in range(33):  # 32**2 == 1024
    if X == 1:
        ans = 1
        break

    for p in range(2, X+1):
        if b**p <= X:
            ans = max(b**p, ans)

print(ans)
