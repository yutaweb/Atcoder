# S = input()
# if S == S[::-1]:
#     print("Yes")
#     exit()
#
# flag = True
# length = len(S) - 1
# while flag:
#     s = S[length]
#     if s == "a":
#         S = "a" + S
#         length = len(S) - 1
#         if S == S[::-1]:
#             print("Yes")
#             flag = False
#     else:
#         print("No")
#         flag = False
#     length -= 1

# 修正 version

def judge():
    S = input()
    l = len(S) - len(S.lstrip('a'))  # 先頭の連続数
    r = len(S) - len(S.rstrip('a'))  # 末尾の連続数
    if l > r: return False
    T = 'a' * (r - l) + S
    return T == T[::-1]

print("Yes" if judge() else "No")