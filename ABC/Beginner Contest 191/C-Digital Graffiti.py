H, W = map(int, input().split())
A = []
for a in range(H):
    A.append(list(input()))

count = 0
for h in range(1, H):
    for w in range(1, W):
        if [A[h-1][w-1], A[h-1][w], A[h][w-1], A[h][w]].count("#")==1 or [A[h-1][w-1], A[h-1][w], A[h][w-1], A[h][w]].count("#")==3:
            count += 1

print(count)