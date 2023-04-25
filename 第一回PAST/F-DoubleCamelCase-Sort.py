# # 計算量：O(10^5)

# ① For文で実装

# S = input()
# Words = []
#
# upper_cnt = 0
# i = 0
# for i in range(len(S)):
#     if S[i].isupper():
#         upper_cnt += 1
#         if upper_cnt % 2 == 0:
#             Words.append(S[start:i+1])
#         else:
#             start = i
#
#
# Words = sorted(Words, key=lambda v: v.upper())
# # Words.sort(key=str.upper())
#
# print(*Words, sep="")

# ② While文で実装
S = input()

Words = []

i = 0
while i < len(S):
    j = i + 1
    while j < len(S) and S[j].islower():
        j += 1

    Words.append(S[i:j+1])

    i = j + 1

Words.sort(key=str.lower)

print("".join(Words))
