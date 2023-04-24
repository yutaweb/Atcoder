# # A
# N = int(input())
# S = input()
#
# split_list = S.split('*')
# if split_list[0].count('|') == 2 or split_list[0].count('|') == 0:
#     ans = 'out'
# else:
#     ans = 'in'
#
# print(ans)
# B
# n, T = map(int, input().split())  # プレイヤー数と場に出されたカードの色を入力する
#
# # プレイヤーが出したカードの色と値を入力する
# colors = list(map(int, input().split()))
# values = list(map(int, input().split()))
#
# # 場に出されたカードの中で値が最大のカードを持つプレイヤーを決定する
# max_value = -1
# winner = -1
# for i in range(n):
#     if colors[i] == T and values[i] > max_value:
#         max_value = values[i]
#         winner = i+1
#
# # もし場にTのカードが出されていなかった場合、プレイヤー1が出した色のカードで最大のものを探す
# if winner == -1:
#     max_value = -1
#     for i in range(n):
#         if colors[i] == colors[0] and values[i] > max_value:
#             max_value = values[i]
#             winner = i+1
#
# print(winner)  # 勝者のプレイヤー番号を出力する

# C
# def is_dango(s):
#     """
#     文字列sがダンゴ文字列であるかどうかを判定する関数。
#     """
#     n = len(s) - 1
#     return (s[0] == '-' and s[1:n] == 'o' * (n - 1) and s[n] == 'o') \
#         or (s[n] == '-' and s[0:n] == 'o' * (n - 1) and s[0] == 'o')
#
# def max_level(s):
#     """
#     文字列sから求められる最大のレベルを返す関数。
#     """
#     max_level = -1
#     for l in range(1, len(s)):
#         for i in range(len(s) - l):
#             if is_dango(s[i:i+l+1]):
#                 max_level = max(max_level, l)
#     return max_level
#
# # 入力を受け取る
# n = int(input())
# s = input()
#
# # 最大のレベルを求める
# x = max_level(s)
#
# # 結果を出力する
# print(x)

