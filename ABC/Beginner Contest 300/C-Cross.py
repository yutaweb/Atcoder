# 連結成分を数え上げる場合
# 計算量：Q(HW)
H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]


def dfs(y, x):
    cnt = 1
    C[y][x] = '.'
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            y2, x2 = y + dy, x + dx
            if 0 <= y2 < H and 0 <= x2 < W and C[y2][x2] == '#':
                cnt += dfs(y2, x2)

    return cnt


ans = [0 for _ in range(min(H, W))]
for i in range(H):
    for j in range(W):
        if C[i][j] == '#':
            ans[dfs(i, j) // 4 - 1] += 1

print(*ans)

# 没解答
# import numpy as np
#
# H, W = map(int, input().split())
# N = min(H, W)
# ans = [0] * N
#
# C = []
# for _ in range(H):
#     C.append(list(input()))
#
# C = np.array(C)
# # print(C)
#
#
# def create_x(size, side):
#     dot = ["." for _ in range(side ** 2)]
#     list_dot = np.array(dot).reshape(side, side)
#
#     # .を#で置換
#     x_middle = y_middle = side // 2
#     list_dot[x_middle][y_middle] = "#"
#
#     for d in range(1, size + 1):
#         list_dot[x_middle + d][y_middle + d] = "#"
#         list_dot[x_middle + d][y_middle - d] = "#"
#         list_dot[x_middle - d][y_middle + d] = "#"
#         list_dot[x_middle - d][y_middle - d] = "#"
#
#     return list_dot


# for i in range(1, N+1):
#     side_l = 1 + 2 * i
#     x = create_x(i, side_l)
#     for w in range(W - side_l + 1):
#         for h in range(H - side_l + 1):
#             print(C[w:w+side_l][h:h+side_l])
# for h in range(1, H):
#     for w in range(1, W):
#         flag = True
#         while flag:
#             if e

# 要復習
