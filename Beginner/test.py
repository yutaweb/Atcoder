import numpy as np
import itertools

# S = np.array(S).T
# T = np.array(T).T.tolist()
# S = S.T
# T = T.T

# print(S, T)
# L = [i for i in range(len(S))]
#
# for index_list in itertools.permutations(L, len(S)):
#     print(S[index_list, :])

# L = [i for i in range(len(S))]
# for index_list in itertools.permutations(L, len(S)):
#     if S.tolist() == T:
#         print("Yes")
#         exit()
#     if S[index_list, :].tolist() == T:
#         print("Yes")
#         exit()
#
# print("No")

# import numpy as np
#
#
# A, B = map(int, input().split())
# g = 1
#
# # fall_time = B * 0 + A / np.sqrt(g)
# # g += 1
# # print(fall_time)
# i = 0
# fall_time = [B * 0 + A / np.sqrt(g)]
# while True:
#     fall_time.append(B * i + A / np.sqrt(g))
#     print(fall_time)
#     if fall_time[i-1] < fall_time[i]:
#         print(fall_time[i-1])
#         exit()
#
#     i += 1
#     g += 1

'''
@Project: algorithm   
@Description: TODO          
@Time:2022/11/26 21:05       
@Author:ZHANG               

'''
# import bisect
# import collections
# import copy
# import fractions
# import itertools
# import math
# import sys
# import heapq
#
# sys.setrecursionlimit(10 ** 9)
# import functools
#
#
# def main(lines):
#     H, W = map(int, lines[0].split(" "))
#     S = collections.Counter(zip(*lines[1:H + 1]))
#     T = collections.Counter(zip(*lines[H + 1:]))
#     if S == T:
#         print("Yes")
#     else:
#         print("No")
#
#
# if __name__ == '__main__':
#     lines = []
#     for l in sys.stdin:
#         lines.append(l.rstrip('\r\n'))
#     main(lines)

