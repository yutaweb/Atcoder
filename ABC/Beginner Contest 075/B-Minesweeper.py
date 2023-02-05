H, W = map(int, input().split())
S = [input() for i in range(H)]

DX = [1, 1, 0, -1, -1, -1, 0, 1]
DY = [0, 1, 1, 1, 0, -1, -1, -1]

# 該当箇所を0で初期化
result = [[0 if v == '.' else '#' for v in row] for row in S]

ans = []
for i in range(H):
    for j in range(W):
        if S[i][j] != ".":
            continue

        for dx, dy in zip(DX, DY):
            ni, nj = i + dx, j + dy

            if ni < 0 or ni >= H or nj < 0 or nj >= W:
                continue

            if S[ni][nj] == '#':
                result[i][j] += 1

for row in result:
    print(*row, sep='')
