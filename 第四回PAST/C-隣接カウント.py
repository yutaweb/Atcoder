H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
count_sharp = [[0 for _ in range(W)] for _ in range(H)]

dx_list = [-1, 0, 1, 1, 1, 0, -1, -1, 0]
dy_list = [-1, -1, -1, 0, 1, 1, 1, 0, 0]

for i, line in enumerate(A):
    for j, point in enumerate(line):
        counter = 0
        for dx, dy in zip(dx_list, dy_list):
            if 0 <= dx + j <= W - 1 and 0 <= dy + i <= H - 1 and A[i + dy][j + dx] == '#':
                counter += 1
            count_sharp[i][j] = counter

for line in count_sharp:
    print(*line, sep="")
