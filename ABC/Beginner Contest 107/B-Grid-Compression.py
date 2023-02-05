H, W = map(int, input().split())
A = [input() for _ in range(H)]

row_ignore = set()
col_ignore = set()

# 縦軸方向に圧縮する対象外のindexを格納
for y in range(H):
    if A[y].count('#') == 0:
        row_ignore.add(y)

for x in range(W):
    temp = [A[y][x] for y in range(H)]
    if temp.count('#') == 0:
        col_ignore.add(x)

ans = []
for y in range(H):
    if y in row_ignore:
        continue
    row = []
    for x in range(W):
        if x in col_ignore:
            continue
        row.append(A[y][x])
    ans.append(row)

for r in ans:
    print(''.join(r))
