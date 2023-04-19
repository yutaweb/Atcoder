from collections import defaultdict


N = int(input())
# defaultdictを使用しない場合、0で初期化する必要がある。
A = defaultdict(int)

for _ in range(N):
    A[int(input())] += 1

cnt = 0
for i in A.keys():
    if A[i] % 2 != 0:
        cnt += 1

print(cnt)

# for _ in range(N):
#     a = int(input())
#     if a in A:
#         # TLE
#         i = A.index(a)
#         A.pop(i)
#     else:
#         A.append(a)
#
# print(len(A))
