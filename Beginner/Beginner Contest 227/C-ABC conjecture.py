# import itertools
#
# count = 0
# N = int(input())
# L = list(itertools.combinations(range(N), 3))
# for val in L:
#     if N <= sum(val):
#         count += 1
#
# print(count)

import math

N = int(input())
ans = 0
for a in range(1, N+1):
	if a*a*a > N: break
	for b in range(a, N+1):
		if a*b*b > N: break
		ans += math.floor(N/(a*b))-b+1
print(ans)

#  方針①
#  1.全通りの組み合わせを考える
#  2.1の中から条件に合致するpatternを抽出する