# import string
#
# S = list(input())
# alphabet = string.ascii_uppercase
#
# if len(S) == 1:
#     ans = alphabet.index(S[0]) + 1
#     exit(print(ans))
#
# counter1 = 0
# for i in range(1, len(S)):
#     for _ in range(alphabet.index(S[0]) + 1):
#         counter1 += 26 ** i
#
# counter2 = 1
# for j in range(len(S)):
#     # counter2 *= (alphabet.index(S[j]) + 1)
#     counter2 = alphabet.index(S[j]) + 1
#
# ans = counter1 + counter2
# print(counter1)
# print(counter2)
# print(ans)
# # counter = len(alphabet) * (len(S) - 1)
# # counter += alphabet.index(S[len(S) - 1]) + 1
# 後で確認する
# def find_question_number(s):
#     question_number = 0
#     for i in range(1, len(s) + 1):
#         question_number += 26 ** (i - 1)
#     for i in range(len(s)):
#         for j in range(ord(s[i]) - ord('A')):
#             question_number += 26 ** (len(s) - i - 1)
#     return question_number
#
#
# S = list(input())
#
# print(find_question_number(S))

def enc(s):
    return ord(s) - ord("A") + 1


S = list(input())

ans = 0
for s in S:
    ans *= 26
    ans += enc(s)

print(ans)

