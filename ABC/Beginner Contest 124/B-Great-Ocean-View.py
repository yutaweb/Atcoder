N = int(input())
H = list(map(int, input().split()))

counter = 0
for i, h in enumerate(H):
    cnt = 0
    for j in range(i + 1):
        if H[j] <= h:
            cnt += 1
    if cnt == i + 1:
        counter += 1

print(counter)
