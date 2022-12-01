from collections import defaultdict
from bisect import bisect

N, M = map(int, input().split())
index = defaultdict(list)
row_data = []

for i in range(M):
    p, y = map(int, input().split())
    row_data.append([p, y])
    index[p].append(y)

for key in index.keys():
    index[key].sort()

for i in range(M):
    rank = bisect(index[row_data[i][0]], row_data[i][1])
    p = row_data[i][0]
    print(str(p).zfill(6) + str(rank).zfill(6))

