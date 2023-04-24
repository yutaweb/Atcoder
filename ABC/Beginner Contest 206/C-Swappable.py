# TLE
# from collections import defaultdict
# import itertools
#
# N = int(input())
# A = list(map(int, input().split()))
#
# DICT = defaultdict(int)
# for key in A:
#     DICT[key] += 1
#
# values = DICT.values()
# ans = 0
# for pair in itertools.combinations(values, 2):
#     ans += pair[0] * pair[1]
#
# print(ans)

# AC 計算量 O(N)
from collections import Counter


N = int(input())
A = list(map(int, input().split()))
C = Counter()

ans = 0
for j in range(N):
    ans += j - C[A[j]]  # j個からj-1個の中でのA[j]の出現回数を引く
    C[A[j]] += 1

print(ans)
