H, W = map(int, input().split())
S = [input() for _ in range(H)]

offsets = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))


def check(x, y):
    c = 'snuke'
    for dx, dy in offsets:
        b = True
        for i in range(1, 5):
            x2 = x + dx * i
            y2 = y + dy * i
            if x2 < 0 or H <= x2 or y2 < 0 or W <= y2 or S[x2][y2] != c[i]:
                b = False
                break
        if b:
            return dx, dy
    return False


for i in range(H):
    for j in range(W):
        if S[i][j] == 's':
            res = check(i, j)
            if res:
                dx, dy = res
                for k in range(5):
                    print(i + dx * k + 1, j + dy * k + 1)

# 冗長バージョン
# import numpy as np
#
#
# H, W = map(int, input().split())
# S = []
# for _ in range(H):
#     S.append(list(input()))
#
# S = np.array(S)
#
# for h in range(H):
#     for w in range(W):
#         # 右
#         if w + 5 <= W and ''.join(S[h][w:w+5]) == 'snuke':
#             ans = [(h + 1, w + 1), (h + 1, w + 2), (h + 1, w + 3), (h + 1, w + 4), (h + 1, w + 5)]
#             break
#         # 左
#         if w - 4 >= 0 and ''.join(reversed(S[h][w-4:w+1])) == 'snuke':
#             ans = [(h + 1, w + 1), (h + 1, w), (h + 1, w - 1), (h + 1, w - 2), (h + 1, w - 3)]
#             break
#         # 下
#         if h + 5 <= H and (S[h][w] == 's' and S[h+1][w] == 'n' and S[h+2][w] == 'u' and S[h+3][w] == 'k' and S[h+4][w] == 'e'):
#             ans = [(h + 1, w + 1), (h + 2, w + 1), (h + 3, w + 1), (h + 4, w + 1), (h + 5, w + 1)]
#             break
#         # 上
#         if h - 4 >= 0 and (S[h][w] == 's' and S[h-1][w] == 'n' and S[h-2][w] == 'u' and S[h-3][w] == 'k' and S[h-4][w] == 'e'):
#             ans = [(h + 1, w + 1), (h, w + 1), (h - 1, w + 1), (h - 2, w + 1), (h - 3, w + 1)]
#             break
#         # 右上
#         if h - 4 >= 0 and w + 5 <= W and (S[h][w] == 's' and S[h-1][w+1] == 'n' and S[h-2][w+2] == 'u' and S[h-3][w+3] == 'k' and S[h-4][w+4] == 'e'):
#             ans = [(h + 1, w + 1), (h, w + 2), (h - 1, w + 3), (h - 2, w + 4), (h - 3, w + 5)]
#             break
#         # 右下
#         if h + 5 <= H and w + 5 <= W and (S[h][w] == 's' and S[h+1][w+1] == 'n' and S[h+2][w+2] == 'u' and S[h+3][w+3] == 'k' and S[h+4][w+4] == 'e'):
#             ans = [(h + 1, w + 1), (h + 2, w + 2), (h + 3, w + 3), (h + 4, w + 4), (h + 5, w + 5)]
#             break
#         # 左上
#         if h - 4 >= 0 and w - 4 >= 0 and (S[h][w] == 's' and S[h-1][w-1] == 'n' and S[h-2][w-2] == 'u' and S[h-3][w-3] == 'k' and S[h-4][w-4] == 'e'):
#             ans = [(h + 1, w + 1), (h, w), (h - 1, w - 1), (h - 2, w - 2), (h - 3, w - 3)]
#             break
#         # 左下
#         if h + 5 <= H and w - 4 >= 0 and (S[h][w] == 's' and S[h+1][w-1] == 'n' and S[h+2][w-2] == 'u' and S[h+3][w-3] == 'k' and S[h+4][w-4] == 'e'):
#             ans = [(h + 1, w + 1), (h + 2, w), (h + 3, w - 1), (h + 4, w - 2), (h + 5, w - 3)]
#             break
#
# for i in range(len(ans)):
#     print('{0} {1}'.format(ans[i][0], ans[i][1]))
#
