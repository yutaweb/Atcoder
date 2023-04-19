# A
# S = list(input())
#
# ans = ""
# for s in S:
#     if s == "0":
#         ans += "1"
#     else:
#         ans += "0"
#
# print(ans)

# B
# N, M = map(int, input().split())
# P = list(map(int, input().split()))
#
# ans = []
# temp = []
# ans = []
# for i in range(1, N+1):
#     if i in P:
#         temp.append(i)
#     else:
#         if i - 1 in P:
#             temp.append(i)
#         if len(temp) != 0:
#             ans.extend(sorted(temp, reverse=True))
#         temp = []
#         if i not in ans:
#             ans.append(i)
#
# ans.extend(sorted(temp, reverse=True))
# print(*ans, sep=' ')

# C
# from itertools import combinations
#
# N, M = map(int, input().split())
# AC = [input() for _ in range(2*M)]
#
# A = {}
# for i, a in enumerate(AC):
#     if i % 2 == 1:
#         A[i] = set(map(int, a.split()))
#
# cnt = 0
# target = set()
# for i in range(1, N+1):
#     target.add(i)
#
# for i in range(1, M+1):
#     for index in list(combinations(A, i)):
#         ans = set()
#         for j in index:
#             ans |= A[j]
#
#         if target == ans:
#             cnt += 1
#
# print(cnt)

# D

