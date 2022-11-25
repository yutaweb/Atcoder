N, X = map(int, input().split())
L = list(map(int, input().split()))

counter = 1
D = 0
for i in range(N):
    D = D + L[i]
    if D <= X:
        counter += 1

print(counter)
