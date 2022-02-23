# TLE
# N = int(input())
# S = input()
# A = [0]
# # point = 0
#
# for i in range(len(S)):
#     if S[i] == "R":
#         A.append(i+1)
#     elif S[i] == "L":
#         A.appendleft(i)
#
# print(*A)

L = []
R = []
N = int(input())
S = input()
for i, s in enumerate(S):
    if s == "L":
        R.append(i)
    else:
        L.append(i)

print(*(L+[N]+R[::-1]))