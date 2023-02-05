N, M = map(int, input().split())

AB = {}
for _ in range(N):
    a, b = map(int, input().split())
    AB[a] = b

print(AB)

sort = sorted(AB.items(), key=lambda x: x[0])
print(sort)
ans = 0
for v in sort:
    quantity = min(v[1], M)
    M -= quantity
    ans += quantity * int(v[0])
    if M == 0:
        print(ans)
        exit()
