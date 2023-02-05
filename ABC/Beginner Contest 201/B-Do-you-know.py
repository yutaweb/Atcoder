N = int(input())
ST = {}

for _ in range(N):
    s, t = input().split()
    ST[s] = int(t)

sort = sorted(ST.items(), key=lambda x: x[1], reverse=True)
print(sort[1][0])

