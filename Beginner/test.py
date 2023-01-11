import numpy as np


# N, M = map(int, input().split())
#
#
# def to_zero_one(ox):
#     ox = ox.replace('o', '1')
#     ox = ox.replace('x', '0')
#     return ox
#
#
# S = [int(to_zero_one(input())) for _ in range(N)]
#
# base = int('1'*M)
# counter = 0
# for i in range(N-1):
#     for j in range(i+1, N):
#         if '0' not in str(S[i] + S[j]).zfill(M):
#             counter += 1
#
# print(counter)
import bisect

# N = int(input())
# S = input().split('"')
#
# for i in range(len(S)):
#     if i % 2 == 0:
#         S[i] = S[i].replace(",", ".")
#
# ans = '"'.join(S)
# print(ans)


