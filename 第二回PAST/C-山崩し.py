N = int(input())
T = [list(input()) for _ in range(N)]

dx_list = [-1, 0, 1]
dy_list = [1, 1, 1]

for y, line in enumerate(reversed(T)):
    y = len(T) - y - 1
    for x, point in enumerate(line):
        for dx, dy in zip(dx_list, dy_list):
            if 1 <= x <= 2 * N - 3 and 0 <= y <= N - 2 and T[y][x] == '#' and T[y][x] != 'X' \
                    and T[y + dy][x + dx] == 'X':
                T[y][x] = 'X'

for line in T:
    print(*line, sep='')
