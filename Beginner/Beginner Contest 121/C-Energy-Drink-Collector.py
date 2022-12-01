N, M = map(int, input().split())

AB = {}
for _ in range(N):
    a, b = input().split()
    AB[a] = int(b)

sort = sorted(AB.items(), key=lambda x: x[0])

# cost = 0
# while M > 0:
sort[0][1] = 3
print(sort[0][1])
print(sort)
